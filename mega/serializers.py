from datetime import datetime

import pytz
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Company, Discount, Social, Rule, Address, Reviews, Customer, Operation, Looking, Telephone


class CompanyListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=40)
    photo = serializers.URLField()
    discount = serializers.IntegerField()
    view_count = serializers.IntegerField()
    city = serializers.CharField()


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class CompanyDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=40)
    photo = serializers.URLField()
    view_count = serializers.IntegerField()
    discount = serializers.IntegerField()
    longitude = serializers.FloatField()
    lantitude = serializers.FloatField()
    address_name = serializers.CharField()
    social = SocialSerializer(many=True)
    rules = serializers.CharField()


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


def exist_operation(customer, discount):
    """Валидация на существующий купон"""
    try:
        Operation.objects.get(discount=discount, customer=customer)
    except Operation.DoesNotExist:
        return True
    raise ValidationError('Вы уже получили купон')


class CuponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = ("customer", "discount",)

    def create(self, validated_data):
        end_date = datetime.now() + validated_data['discount'].end_date_cupon
        coupon = Operation.objects.create(discount=validated_data['discount'],
                                          customer=validated_data['customer'],
                                          end_date=end_date)
        return coupon

    def validate(self, data):
        discount = data['discount']
        customer = data['customer']

        amount_coupons = Operation.objects.filter(discount=data['discount'], status__in=['1', '2'])

        if exist_operation(customer, discount):
            if len(amount_coupons) >= Company.objects.get(discount=discount).limit:
                discount.dis.company.active = False
                discount.dis.company.save()
                raise ValidationError("Превышен лимит")
            return data


class ActivateCouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = ("pin", "customer", "discount")

    def validate(self, data):
        pin = data['pin']
        discount = data['discount']
        customer = data['customer']
        status = Operation.objects.get(discount_id=discount.id, customer_id=customer.id).status
        end_date_cupon = Operation.objects.get(discount_id=discount.id, customer_id=customer.id).end_date_cupon
        local_tz = pytz.timezone('Asia/Kolkata')
        current_datetime = datetime.now().replace(tzinfo=pytz.utc).astimezone(local_tz)
        expired_on = end_date_cupon.replace(tzinfo=pytz.utc).astimezone(local_tz)
        if current_datetime >= expired_on:
            Operation.objects.update(status='3')
            raise ValidationError('Срок действия купона завершен')
        elif pin != int(discount.pin):
            raise ValidationError('Неверный пин код')
        elif status == '1':
            raise ValidationError('Купон уже активирован')
        return data