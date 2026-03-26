from django.contrib import admin
from django.urls import path
from pages import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('ideas/', views.ideas, name='ideas'),
    path('categories/', views.categories, name='categories'),
]