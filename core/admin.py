from django.contrib import admin
from .models import ExamCategory, ExamResource, UserProfile, SavedResource, SearchLog


@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(ExamResource)
class ExamResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'source_name', 'difficulty', 'exam_type', 'subject', 'is_free', 'is_active']
    list_filter = ['category', 'difficulty', 'exam_type', 'is_free', 'is_active']
    search_fields = ['title', 'description', 'source_name']
    list_editable = ['is_active']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'target_exam', 'created_at']


@admin.register(SavedResource)
class SavedResourceAdmin(admin.ModelAdmin):
    list_display = ['user', 'resource', 'saved_at', 'is_completed']
    list_filter = ['is_completed']


@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'results_count', 'searched_at']
    readonly_fields = ['user', 'query', 'results_count', 'searched_at']
