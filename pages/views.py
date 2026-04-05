from django.shortcuts import render
from .models import Idea

def index(request):
    latest_ideas = Idea.objects.filter(is_active=True)[:3]
    
    context = {
        'title': 'Копилка идей для свиданий',
        'site_name': 'DateIdeas',
        'description': '100+ способов удивить вторую половинку. Здесь собраны идеи на любой вкус: от романтических пикников до активных приключений.',
        'ideas': latest_ideas,
        'ideas_count': Idea.objects.filter(is_active=True).count(),
    }
    return render(request, 'pages/index.html', context)

def ideas(request):
    all_ideas = Idea.objects.filter(is_active=True)
    
    context = {
        'all_ideas': all_ideas,
        'total_count': all_ideas.count(),
    }
    return render(request, 'pages/ideas.html', context)

def categories(request):
    categories_list = []
    for category_code, category_name in Idea.CATEGORY_CHOICES:
        count = Idea.objects.filter(category=category_code, is_active=True).count()
        categories_list.append({
            'code': category_code,
            'name': category_name,
            'description': get_category_description(category_code),
            'ideas_count': count
        })
    
    context = {
        'categories': categories_list,
    }
    return render(request, 'pages/categories.html', context)

def get_category_description(category_code):
    descriptions = {
        'romantic': 'Идеи для создания особой атмосферы и незабываемых моментов',
        'adventure': 'Активный отдых, квесты и экстремальные развлечения',
        'creative': 'Мастер-классы, рисование, музыка и другие творческие занятия',
        'culture': 'Театры, выставки, музеи и концерты',
        'active': 'Спорт, прогулки и физическая активность вдвоем',
        'home': 'Уютные вечера дома, совместное приготовление еды и киномарафоны',
    }
    return descriptions.get(category_code, 'Интересные идеи для свиданий')