from django.shortcuts import render, get_object_or_404, redirect /Django'da view, kullanıcı bir sayfaya girdiğinde çalışan fonksiyondur. Her URL'nin bir view'u var.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

from .models import ExamCategory, ExamResource, SavedResource, SearchLog
from .forms import RegisterForm, ProfileEditForm


def home(request): Ana sayfaya girilince tüm kategorileri ve son 6 kaynağı veritabanından çekip HTML'e gönderiyorum."
    categories = ExamCategory.objects.all()
    latest_resources = ExamResource.objects.filter(is_active=True).select_related('category')[:6]
    return render(request, 'core/home.html', {
        'categories': categories,
        'latest_resources': latest_resources,
    })


def search(request):"Kullanıcı arama yaptığında URL şöyle oluyor: /search/?q=SAT. request.GET.get('q') ile o kelimeyi alıyorum, ai_search fonksiyonuna gönderiyorum, sonuçları SearchLog'a kaydediyorum, sayfayı render ediyorum."
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        from .ai_search import live_search
        results = live_search(query)

        SearchLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            query=query,
            results_count=len(results)
        )

    return render(request, 'core/search_results.html', {
        'query': query,
        'results': results,
        'results_count': len(results),
    })


def resource_detail(request, pk): 
    resource = get_object_or_404(ExamResource, pk=pk, is_active=True)
    saved_resource = None
    if request.user.is_authenticated:
        saved_resource = SavedResource.objects.filter(user=request.user, resource=resource).first()
    related = ExamResource.objects.filter(
        category=resource.category, is_active=True
    ).exclude(pk=pk)[:3]
    return render(request, 'core/resource_detail.html', {
        'resource': resource,
        'saved_resource': saved_resource,
        'related': related,
    })


@login_required
def dashboard(request):"Dashboard, kaydetme gibi işlemlere giriş yapmadan erişince otomatik login sayfasına atıyor. Bunu her view'a tek satırla ekliyorum
    saved_count = SavedResource.objects.filter(user=request.user).count()
    completed_count = SavedResource.objects.filter(user=request.user, is_completed=True).count()
    recent_searches = SearchLog.objects.filter(user=request.user)[:5]
    profile = request.user.userprofile
    return render(request, 'core/dashboard.html', {
        'saved_count': saved_count,
        'completed_count': completed_count,
        'recent_searches': recent_searches,
        'profile': profile,
    })


@login_required
def saved_tests(request):
    saved = SavedResource.objects.filter(user=request.user).select_related('resource', 'resource__category')
    total = saved.count()
    completed = saved.filter(is_completed=True).count()
    return render(request, 'core/saved_tests.html', {
        'saved_resources': saved,
        'total': total,
        'completed': completed,
    })


@login_required
def save_resource(request, pk=None): kayıt varsa getir, yoksa oluştur' diyor. Eğer zaten kaydedilmişse siliyorum, yoksa ekliyorum.  Sayfa yenilenmeden çalışıyor çünkü JsonResponse döndürüyorum, JavaScript bunu yakalar."
    """Save a resource. pk=None means create from POST data (live search result)."""
    if request.method == 'POST':
        import json as json_lib
        data = json_lib.loads(request.body)

        if pk:
            resource = get_object_or_404(ExamResource, pk=pk)
        else:
            url = data.get('url', '')
            title = data.get('title', '')
            description = data.get('description', '')
            source_name = data.get('source', '')

            if not url or not title:
                return JsonResponse({'error': 'Missing data'}, status=400)

            default_category, _ = ExamCategory.objects.get_or_create(
                slug='general',
                defaults={
                    'name': 'General',
                    'region': 'INTERNATIONAL',
                    'description': 'General exam resources'
                }
            )

            resource, created = ExamResource.objects.get_or_create(
                url=url,
                defaults={
                    'title': title[:255],
                    'category': default_category,
                    'source_name': source_name[:100] if source_name else 'Web',
                    'description': description[:1000] if description else '',
                    'difficulty': 'MEDIUM',
                    'exam_type': 'FULL_TEST',
                    'subject': 'General',
                    'is_free': True,
                    'is_active': True,
                }
            )

        saved_obj = SavedResource.objects.filter(user=request.user, resource=resource).first()
        if saved_obj:
            saved_obj.delete()
            saved = False
        else:
            SavedResource.objects.create(user=request.user, resource=resource)
            saved = True

        count = SavedResource.objects.filter(user=request.user).count()
        return JsonResponse({'saved': saved, 'count': count, 'resource_id': resource.pk})

    return JsonResponse({'error': 'POST required'}, status=405)


@login_required
@require_POST
def toggle_complete(request, pk):
    saved = get_object_or_404(SavedResource, pk=pk, user=request.user)
    saved.is_completed = not saved.is_completed
    saved.save()
    return JsonResponse({'completed': saved.is_completed})


@login_required
@require_POST
def update_notes(request, pk):
    saved = get_object_or_404(SavedResource, pk=pk, user=request.user)
    saved.notes = request.POST.get('notes', '')
    saved.save()
    return JsonResponse({'success': True})


@login_required
def profile_edit(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'core/profile_edit.html', {'form': form})


class RegisterView(View): Kayıt sayfası class olarak yazıldı. GET isteği gelince formu gösteriyor, POST gelince formu kaydedip kullanıcıyı otomatik giriş yaptırıyor ve dashboard'a yönlendiriyor."
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Your account has been created.')
            return redirect('dashboard')
        return render(request, 'registration/register.html', {'form': form})
