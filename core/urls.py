from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('saved/', views.saved_tests, name='saved_tests'),
    path('save/', views.save_resource, name='save_resource_new'),  # for live results
    path('save/<int:pk>/', views.save_resource, name='save_resource'),
    path('complete/<int:pk>/', views.toggle_complete, name='toggle_complete'),
    path('notes/<int:pk>/', views.update_notes, name='update_notes'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
# Her URL bir view'a bağlı. <int:pk> dinamik kısım, oraya gelen sayıyı view'a parametre olarak geçiyor. name= ile URL'lere isim verdim, HTML'de {% url 'home' %} diyerek kullandım, URL değişse bile HTML bozulmuyor.
