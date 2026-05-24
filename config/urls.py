from django.contrib import admin
from django.urls import path, include
from pages import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('', views.index, name='home'),
    path('ideas/', views.ideas, name='ideas'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:category_slug>/', views.category_ideas, name='category_ideas'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('contact/', views.contact, name='contact'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', views.idea_update, name='idea_update'),
]