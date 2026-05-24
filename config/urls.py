from django.contrib import admin
from django.urls import path, include
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('', views.HomeView.as_view(), name='home'),
    path('ideas/', views.IdeaListView.as_view(), name='ideas'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:category_slug>/', views.category_ideas, name='category_ideas'),
    path('idea/<int:pk>/', views.IdeaDetailView.as_view(), name='idea_detail'),
    path('contact/', views.contact, name='contact'),
    path('idea/create/', views.IdeaCreateView.as_view(), name='idea_create'),
    path('idea/<int:pk>/edit/', views.IdeaUpdateView.as_view(), name='idea_update'),
    path('idea/<int:pk>/delete/', views.IdeaDeleteView.as_view(), name='idea_delete'),
    path('tag/<str:tag_name>/', views.tag_ideas, name='tag_ideas'),
    path('idea/<int:pk>/comment/', views.add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)