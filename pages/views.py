from django.shortcuts import render

def index(request):
    context = {
        'title': 'Копилка идей для свиданий',
        'site_name': 'DateIdeas',
        'description': '100+ способов удивить вторую половинку. Здесь собраны идеи на любой вкус: от романтических пикников до активных приключений. Сохраняйте понравившиеся, делитесь своими и вдохновляйтесь!',
        'ideas': [
            {
                'title': 'Пикник на крыше',
                'description': 'Плед, горячий чай и закат над городом. Бесплатно и очень романтично.',
                'image': 'https://placehold.co/300x200?text=Пикник+на+крыше'
            },
            {
                'title': 'Гончарный МК',
                'description': 'Создайте своими руками кружку или тарелку. Останется память на долгие годы.',
                'image': 'https://placehold.co/300x200?text=Гончарный+МК'
            },
            {
                'title': 'Квест-комната',
                'description': 'Проверка команды на прочность. Выбирайте хоррор или детектив.',
                'image': 'https://placehold.co/300x200?text=Квест+комната'
            }
        ]
    }
    return render(request, 'pages/index.html', context)

def ideas(request):
    all_ideas = [
        {
            'title': 'Пикник на крыше',
            'description': 'Плед, горячий чай и закат над городом. Бесплатно и очень романтично.',
            'category': 'Романтика',
            'budget': 'Бесплатно',
            'image': 'https://placehold.co/300x200?text=Пикник'
        },
        {
            'title': 'Гончарный мастер-класс',
            'description': 'Создайте своими руками кружку или тарелку. Останется память на долгие годы.',
            'category': 'Творчество',
            'budget': '2000-3000₽',
            'image': 'https://placehold.co/300x200?text=Гончарный+МК'
        },
        {
            'title': 'Квест-комната',
            'description': 'Проверка команды на прочность. Выбирайте хоррор или детектив.',
            'category': 'Приключения',
            'budget': '2500-4000₽',
            'image': 'https://placehold.co/300x200?text=Квест'
        },
        {
            'title': 'Ужин при свечах дома',
            'description': 'Приготовьте вместе ужин, накройте красиво стол и создайте романтическую атмосферу.',
            'category': 'Романтика',
            'budget': '1000-2000₽',
            'image': 'https://placehold.co/300x200?text=Ужин'
        },
        {
            'title': 'Прогулка на лошадях',
            'description': 'Романтическая прогулка верхом на закате. Незабываемые впечатления гарантированы.',
            'category': 'Активный отдых',
            'budget': '3000-5000₽',
            'image': 'https://placehold.co/300x200?text=Лошади'
        },
        {
            'title': 'Посещение планетария',
            'description': 'Наблюдение за звездами и космические тайны создают особую атмосферу романтики.',
            'category': 'Культура',
            'budget': '500-1000₽',
            'image': 'https://placehold.co/300x200?text=Планетарий'
        }
    ]
    context = {
        'all_ideas': all_ideas
    }
    return render(request, 'pages/ideas.html', context)

def categories(request):
    categories_list = [
        {
            'name': 'Романтика',
            'description': 'Идеи для создания особой атмосферы и незабываемых моментов',
            'ideas_count': 15
        },
        {
            'name': 'Приключения',
            'description': 'Активный отдых, квесты и экстремальные развлечения',
            'ideas_count': 12
        },
        {
            'name': 'Творчество',
            'description': 'Мастер-классы, рисование, музыка и другие творческие занятия',
            'ideas_count': 10
        },
        {
            'name': 'Культура',
            'description': 'Театры, выставки, музеи и концерты',
            'ideas_count': 18
        },
        {
            'name': 'Активный отдых',
            'description': 'Спорт, прогулки и физическая активность вдвоем',
            'ideas_count': 14
        },
        {
            'name': 'Домашний уют',
            'description': 'Уютные вечера дома, совместное приготовление еды и киномарафоны',
            'ideas_count': 20
        }
    ]
    context = {
        'categories': categories_list
    }
    return render(request, 'pages/categories.html', context)