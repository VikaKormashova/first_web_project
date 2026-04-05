from django.db import models

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
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Идея для свидания'
        verbose_name_plural = 'Идеи для свиданий'
        ordering = ['-created_at']