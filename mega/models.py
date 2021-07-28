from datetime import datetime

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=40)
    photo = models.ImageField("Изображение")
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    address = models.ForeignKey("Address", on_delete=models.DO_NOTHING)
    discount = models.ForeignKey("Discount", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Telephone(models.Model):
    number = models.IntegerField()
    company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.number


class Looking(models.Model):
    id = models.ForeignKey(Company, on_delete=models.DO_NOTHING, primary_key=True)
    counter = models.IntegerField()

    def __str__(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Social(models.Model):
    urls = models.SlugField()
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Discount(models.Model):
    percent = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=12, day=31))
    rules = models.ForeignKey("Rule", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.percent


class Rule(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Address(models.Model):
    longitude = models.FloatField(max_length=20)
    latitude = models.FloatField(max_length=20)
    city = models.ForeignKey("City", on_delete=models.DO_NOTHING)
    address_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}'


class Reviews(models.Model):
    review = models.CharField(max_length=100)
    id_company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)
    id_customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Operation(models.Model):
    status = models.CharField(max_length=50)
    id_customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    id_company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(default=datetime(year=2999, month=12, day=31))


class City(models.Model):
    name = models.CharField(max_length=100)
    order_num = models.IntegerField()