from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название тега')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Idea(models.Model):
    
    CATEGORY_CHOICES = [
        ('romantic', 'Романтика'),
        ('adventure', 'Приключения'),
        ('creative', 'Творчество'),
        ('culture', 'Культура'),
        ('active', 'Активный отдых'),
        ('home', 'Домашний уют'),
    ]
    
    BUDGET_CHOICES = [
        ('free', 'Бесплатно'),
        ('low', 'Бюджетно (до 1000₽)'),
        ('medium', 'Средний (1000-3000₽)'),
        ('high', 'Высокий (3000-10000₽)'),
        ('luxury', 'Премиум (10000₽+)'),
    ]
    
    title = models.CharField(
        max_length=200,
        verbose_name='Название идеи'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='romantic',
        verbose_name='Категория'
    )
    budget = models.CharField(
        max_length=20,
        choices=BUDGET_CHOICES,
        default='medium',
        verbose_name='Бюджет'
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на изображение'
    )
    image = models.ImageField(
        upload_to='ideas_images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    duration_hours = models.IntegerField(
        default=2,
        verbose_name='Длительность (часы)'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Автор',
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='ideas', verbose_name='Теги')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Идея для свидания'
        verbose_name_plural = 'Идеи для свиданий'
        ordering = ['-created_at']

class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return f'Комментарий от {self.author.username} к {self.idea.title}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']