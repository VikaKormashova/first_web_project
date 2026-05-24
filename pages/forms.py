from django import forms
from .models import Idea

class FeedbackForm(forms.Form):
    
    subject = forms.CharField(
        label='Тема сообщения',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Например: Вопрос о свидании'
        })
    )
    
    email = forms.EmailField(
        label='Ваш Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@mail.ru'
        })
    )
    
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Напишите ваше сообщение здесь...'
        })
    )

class IdeaForm(forms.ModelForm):
    
    class Meta:
        
        model = Idea
        fields = ['title', 'description', 'category', 'budget', 'duration_hours', 'image_url', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Пикник на крыше'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Подробное описание идеи...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'budget': forms.Select(attrs={'class': 'form-select'}),
            'duration_hours': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Название идеи',
            'description': 'Описание',
            'category': 'Категория',
            'budget': 'Бюджет',
            'duration_hours': 'Длительность (часы)',
            'image_url': 'Ссылка на изображение (опционально)',
            'is_active': 'Активна',
        }