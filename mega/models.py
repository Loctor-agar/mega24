from datetime import datetime, timedelta

from django.db import models

# Create your models here.


class Company(models.Model):
    # Компании
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=40)
    photo = models.URLField()
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    address = models.ForeignKey("Address", on_delete=models.DO_NOTHING)
    discount = models.ForeignKey("Discount", on_delete=models.DO_NOTHING, related_name="dis")
    limit = models.IntegerField("Лимит на скидки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = "Компании"


class Telephone(models.Model):
    # Телефоны компаний
    number = models.CharField(max_length=15)
    company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = "Телефоны"


class Looking(models.Model):
    # Просмотры компаний
    id = models.ForeignKey("Company", primary_key=True, unique=True, on_delete=models.CASCADE)
    counter = models.IntegerField("Количество просмотров",
                                  default=0)

    def __str__(self):
        return str(self.counter)

    class Meta:
        verbose_name = 'Просмотр'
        verbose_name_plural = "Просмотры"


class Category(models.Model):
    # Категории компаний
    name = models.CharField("Название категории", max_length=50)
    order_num = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Social(models.Model):
    # Социальные сети Компаний
    urls = models.URLField()
    name = models.CharField(max_length=100)
    choices = [('Instagram', 'Instagram'),
               ('Facebook', 'Facebook'),
               ('Youtube', 'Youtube')]
    type = models.CharField(max_length=200, choices=choices)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = "Соц.сети"


class Discount(models.Model):
    # Скидки для компаний
    pin = models.IntegerField("Пин код")
    order_num = models.IntegerField()
    end_date_cupon = models.DurationField("Период купона", default=timedelta())
    percent = models.IntegerField("Процент")
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=12, day=31))
    rules = models.ForeignKey("Rule", on_delete=models.DO_NOTHING)
    active = models.BooleanField("Активный или нет", default=True)

    def __str__(self):
        return f'{self.percent}, {self.rules}'

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = "Скидки"


class Rule(models.Model):
    # Условия для компаний
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = "Условия"


class Address(models.Model):
    # Адресса компаний с долготой и широтой
    longitude = models.FloatField("Долгота", max_length=20)
    latitude = models.FloatField("Широта", max_length=20)
    city = models.ForeignKey("City", on_delete=models.DO_NOTHING, verbose_name="Город")
    address_name = models.CharField("Название адресса",max_length=50)

    def __str__(self):
        return f'{self.address_name}'

    class Meta:
        verbose_name = 'Адресс'
        verbose_name_plural = "Адресса"


class Reviews(models.Model):
    # Отзывы
    review = models.CharField("Отзыв", max_length=100)
    company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)
    customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.review} - {self.company} - {self.customer}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"


class Customer(models.Model):
    # Пользователи
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


class Operation(models.Model):
    # Активация купона
    choose = [('Active', 'Активирован'), ('Blocked', 'Заблонирован'), ('Expired', 'Просрочен')]
    status = models.CharField(max_length=150, choices=choose)
    customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    discount = models.ForeignKey("Discount", on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=12, day=31))

    def __str__(self):
        return f'{self.status} - {self.discount} - {self.end_date}'

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = "Операции"


class City(models.Model):
    # Города
    name = models.CharField(max_length=100)
    order_num = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"