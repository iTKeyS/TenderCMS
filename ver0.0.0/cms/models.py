from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
#

###Хрен знает что это но без неё будет ошибка БД

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

###Каталог хранения

class Category(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    slug = models.SlugField('Путь до категории', max_length=40, unique=True)
    description = models.CharField('Описание', max_length=70)
    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

        def __str__(self):
            return self.title

###Сама БД и ее содержимое со всеми столбцами

class Post(models.Model):

###Здесь статусы и их перечень

    STATUS_ZAEVKI = (
        ('good', 'Готова'),
        ('podana', 'Подана'),
        ('none', 'Нет'),
    )
    STATUS_AUKCION = (
        ('torg', 'Торгуемся'),
        ('win', 'Выйграли'),
        ('dewin', 'Проиграли'),
        ('brak', 'Брак'),
        ('none', 'Нет'),
    )
    STATUS_KONTRAKT = (
        ('polbankgar', 'Получение банковской гарантии'),
        ('sogbankgar', 'Согласование банковской гарантии'),
        ('poduc', 'Подписан участником'),
        ('podzac', 'Подписан заказчиком'),
        ('podkvip', 'Подготовка к выполнению'),
        ('ispolnenie', 'Исполнение'),
        ('ispolnen', 'Исполнен'),
        ('rastorgnut', 'Расторгнут'),
        ('none', 'Нет'),
    )
    STATUS_OGRANICENIA = (
        ('none', 'Нет'),
        ('yes', 'Да'),
    )
    STATUS_PLOSHADKI = (
        ('РТС', 'РТС'),
        ('Сбербанк', 'Сбербанк'),
        ('Нет', 'Нет'),
    )
    STATUS_SHAG = (
        ('Новое', 'Новое'),
        ('В работу', 'В работу'),
        ('Выйгранные', 'Выйгранные'),
        ('Проигранные', 'Проигранные'),
        ('Отбракованные', 'Отбракованные'),
        ('Заключенные контракты', 'Заключенные контракты'),
    )

###Здесь текстовая инфа

    id          = models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID'
                )
    slug        = models.SlugField(
                'Номер извещения',
                max_length=30,
                unique=True,
                default="Обязательное поле"
                )
    title       = models.TextField(
                "Предмет закупки",
                max_length=800,
                default="Обязательное поле"
                )
    content     = models.CharField(
                'Заказчик',
                max_length=400,
                default="Обязательное поле"
                )
    n_e_p_v_i_s = models.CharField(
                "Площадка",
                max_length=30,
                default="Нет",
                choices=STATUS_PLOSHADKI
                )
    o_p_r_d     = models.TextField(
                'Ограничения по разрешительной документации',
                max_length=250,
                default="none",
                choices=STATUS_OGRANICENIA
                )
    o_p_r_d_t   = models.TextField(
                'Ограничения по разрешительной документации: подробности',
                max_length=250,
                default="Какие?",
                )
    p_b         = models.TextField(
                'Причина брака',
                max_length=250,
                default='Нет'
                )

###Здесь цифровая инфа

    n_c_k    = models.FloatField(
            "Начальная цена контракта",
            default=0
            )
    r_o_z    = models.FloatField(
            "Размер обеспечения заявок",
            default=0
            )
    r_o_i_k  = models.FloatField(
            "Размер обеспечения исполнения контракта",
            default="0"
            )
    sebis    = models.FloatField(
            'Себестоимость',
            default=0
            )
    c_p      = models.CharField(
            'Ценовой порог',
            max_length=20,
            default=0
            )
    s_b_g    = models.FloatField(
            'Стоимость банковской гарантии',
            default=0
            )
    c_c     = models.FloatField(
            'Цена контракта',
            default=0
            )
    c_k_p   = models.FloatField(
            'Цена контракта плановая',
            default=0
            )
    c_k_f   = models.FloatField(
            'Цена контракта фактическая',
            default=0
            )
    f_s     = models.FloatField(
            'Фактическая себестоимость',
            default=0
            )
    c_k     = models.FloatField(
            'Цена конкурента',
            default=0
            )
    p_s     = models.FloatField(
            'Плановая себестоимость',
            default=0
            )

###Здесь временная инфа

    d_p_a_v_e_f     = models.DateField(
                    "Дата проведения аукциона",
                    default=timezone.now
                    )
    d_p_b_o         = models.DateField(
                    "Дата подбора (выхода)",
                    default=timezone.now
                    )
    d_t_o_p_z       = models.DateTimeField(
                    "Дата и время окончания подачи заявок",
                    default=timezone.now
                    )
    s_p_r           = models.DateField(
                    'Срок производства работ',
                    default=timezone.now
                    )
    s_p_k           = models.DateField(
                    'Срок подписания контракта',
                    default=timezone.now
                    )
    s_v_r           =models.CharField(
                    'Срок выполнения работ',
                    default=0,
                    max_length=40,
                    )
    published       = models.DateTimeField(
                    'Опубликованно',
                    default=timezone.now
                    )
    created         = models.DateTimeField(
                    'Создано',
                    auto_now_add=True
                    )
    updated         = models.DateTimeField(
                    'Обновлено',
                    auto_now=True
                    )

###Здесь статусная инфа

    s_s_a       = models.CharField(
                'Статус шага аукциона',
                max_length=16,
                choices=STATUS_SHAG,
                default='Новое'
                )
    s_k         = models.CharField(
                'Статус контракта',
                max_length=14,
                choices=STATUS_KONTRAKT,
                default='none'
                )
    s_a         = models.CharField(
                'Статус аукциона',
                max_length=14,
                choices=STATUS_AUKCION,
                default='none'
                )
    status      = models.CharField(
                'Статус заявки', max_length=14,
                choices=STATUS_ZAEVKI,
                default='none'
                )
    category    = models.ForeignKey(
                Category,
                on_delete=models.SET_NULL,
                null=True,
                default='1'
                )

###Здесь инфа о пользователях

    user    = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.SET(get_sentinel_user)
            )

###Пошли атрибуты

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

###Коментарии

class Comment(models.Model):
    pass
"""
    post        = models.ForeignKey(
                'Комментарий',
                Post,
                related_name='comments',
                on_delete=models.SET_NULL,
                null=True
                )
    user        = models.CharField(
                'Пользователь',
                max_length=250
                )
    email       = models.EmailField(
                'Почтовый адрес'
                )
    body        = models.TextField(
                'Содержание комментария'
                )
    created     = models.DateTimeField(
                'Создано',
                auto_now_add=True
                )
    approved    = models.BooleanField(
                'Обновлено',
                default=False
                )

###Пошли атрибуты

    def approved(self):
        self.approved = True
        self.save()

        def __str__(self):
            return self.user
"""
