from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea
from .forms import FeedbackForm, IdeaForm

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

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk, is_active=True)
    
    context = {
        'idea': idea,
    }
    return render(request, 'pages/detail.html', context)

def contact(request):
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print("=" * 50)
            print("НОВОЕ СООБЩЕНИЕ С САЙТА")
            print(f"Тема: {cleaned_data['subject']}")
            print(f"Email: {cleaned_data['email']}")
            print(f"Сообщение: {cleaned_data['text']}")
            print("=" * 50)
            
            return redirect('home')
    else:
        form = FeedbackForm()
    
    context = {
        'form': form,
        'title': 'Обратная связь',
    }
    return render(request, 'pages/contact.html', context)

def idea_create(request):
    
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    
    context = {
        'form': form,
        'title': 'Добавить новую идею',
        'button_text': 'Создать',
    }
    return render(request, 'pages/idea_form.html', context)

def idea_update(request, pk):
    
    idea = get_object_or_404(Idea, pk=pk)
    
    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    
    context = {
        'form': form,
        'title': f'Редактирование: {idea.title}',
        'button_text': 'Сохранить',
    }
    return render(request, 'pages/idea_form.html', context)