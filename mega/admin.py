from django.contrib import admin

# Register your models here.
from .models import Company, Discount, Social, Rule, Address, Reviews, Customer, Operation, Looking, Telephone, City, Category

admin.site.register(Company)
admin.site.register(Discount)
admin.site.register(Social)
admin.site.register(Rule)
admin.site.register(Address)
admin.site.register(Reviews)
admin.site.register(Customer)
admin.site.register(Looking)
admin.site.register(Operation)
admin.site.register(Telephone)
admin.site.register(City)
admin.site.register(Category)