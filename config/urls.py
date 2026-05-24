from django.contrib import admin
from django.urls import path, include
from pages import views  
from django.conf import settings
from django.conf.urls.static import static

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
    path('tag/<str:tag_name>/', views.tag_ideas, name='tag_ideas'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)