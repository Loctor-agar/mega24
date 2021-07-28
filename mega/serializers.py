from rest_framework import serializers

from .models import Company, Discount, Social, Rule, Address, Reviews, Customer, Operation, Looking, Telephone


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
