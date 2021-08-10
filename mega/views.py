from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .dtos import get_dto_list_company, get_dto_detail_company, get_dto_reviews, CompanyDto, CompanyDetailDto
from .models import Company, Reviews, Operation
from .serializers import CompanyListSerializer, CompanyDetailSerializer, ReviewsSerializer, CuponSerializer, \
    ActivateCouponSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .services.view_service import get_object, counts_views


class CompanyList(ListAPIView):
    serializer_class = CompanyListSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query_param = self.request.query_params
        queryset = get_dto_list_company(query_param)
        return queryset


class CompanyDetail(ListAPIView):
    queryset = get_dto_detail_company()
    serializer_class = CompanyDetailSerializer

    def get(self, request, pk):
        company = get_object(pk)
        company_dto = CompanyDetailDto(company)
        counts_views(company)
        serializer = CompanyDetailSerializer(company_dto)
        return Response(serializer.data)


class CuponCreate(APIView):
    # Создание и вывод купона
    def get(self, request):
        operation = Operation.objects.all()
        serializer = CuponSerializer(operation, many=True)
        return Response(serializer.data)

    def post(self, request):
        operation = request.data
        serializer = CuponSerializer(data=operation)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response()


def exist_customer_discount(discount_id, customer_id):
    try:
        return Operation.objects.get(discount=discount_id, customer=customer_id)
    except Operation.DoesNotExist:
        raise ValidationError()


class ActivateCoupon(APIView):
    # Активация купона

    def post(self, request):
        serializer = ActivateCouponSerializer(data=request.data)
        if serializer.is_valid():
            discount_id, customer_id = serializer.data['discount'], serializer.data['client']
            operation = exist_customer_discount(discount_id, customer_id)
            operation.status = '1'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewsCreate(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer




