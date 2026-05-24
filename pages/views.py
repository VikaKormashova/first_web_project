from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Idea, Tag, Comment
from .forms import FeedbackForm, IdeaForm, CommentForm

class HomeView(ListView):
    model = Idea
    template_name = 'pages/index.html'
    context_object_name = 'ideas'
    
    def get_queryset(self):
        return Idea.objects.filter(is_active=True)[:3]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Копилка идей для свиданий'
        context['site_name'] = 'DateIdeas'
        context['description'] = '100+ способов удивить вторую половинку. Здесь собраны идеи на любой вкус: от романтических пикников до активных приключений.'
        context['ideas_count'] = Idea.objects.filter(is_active=True).count()
        return context

class IdeaListView(ListView):
    model = Idea
    template_name = 'pages/ideas.html'
    context_object_name = 'all_ideas'
    
    def get_queryset(self):
        return Idea.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = self.get_queryset().count()
        return context

class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'pages/detail.html'
    context_object_name = 'idea'
    
    def get_queryset(self):
        return Idea.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class IdeaCreateView(LoginRequiredMixin, CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'pages/idea_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Идея успешно создана!')
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новую идею'
        context['button_text'] = 'Создать'
        return context

class IdeaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'pages/idea_form.html'
    
    def test_func(self):
        idea = self.get_object()
        return idea.author == self.request.user
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Идея успешно обновлена!')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование: {self.object.title}'
        context['button_text'] = 'Сохранить'
        return context

class IdeaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Idea
    template_name = 'pages/idea_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        idea = self.get_object()
        return idea.author == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Идея успешно удалена!')
        return super().delete(request, *args, **kwargs)

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return response

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

def category_ideas(request, category_slug):
    category_mapping = {
        'romantic': 'Романтика',
        'adventure': 'Приключения',
        'creative': 'Творчество',
        'culture': 'Культура',
        'active': 'Активный отдых',
        'home': 'Домашний уют',
    }
    
    category_name = category_mapping.get(category_slug, 'Категория')
    ideas = Idea.objects.filter(category=category_slug, is_active=True)
    
    context = {
        'category_name': category_name,
        'category_slug': category_slug,
        'ideas': ideas,
        'ideas_count': ideas.count(),
    }
    return render(request, 'pages/category_ideas.html', context)

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
            messages.success(request, 'Сообщение отправлено!')
            return redirect('home')
    else:
        form = FeedbackForm()
    
    context = {
        'form': form,
        'title': 'Обратная связь',
    }
    return render(request, 'pages/contact.html', context)

def tag_ideas(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    ideas = tag.ideas.filter(is_active=True)
    
    context = {
        'tag_name': tag_name,
        'ideas': ideas,
        'ideas_count': ideas.count(),
    }
    return render(request, 'pages/tag_ideas.html', context)

@login_required
def add_comment(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.author = request.user
            comment.save()
            messages.success(request, 'Ваш комментарий успешно добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении комментария.')
    
    return redirect('idea_detail', pk=idea.pk)