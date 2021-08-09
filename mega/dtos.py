from itertools import chain

from .models import Looking, Company, Social, Reviews


class CompanyDto:
    def __init__(self, company):
        self.id = company.id
        self.name = company.name
        self.description = company.description
        self.city = company.address.city
        self.status = company.status
        self.photo = company.photo
        self.discount = company.discount.percent
        self.view_count = Looking.objects.get(id=company).counter


def get_dto_list_company(query_param):
    category = query_param.get('category')
    city = query_param.get('city')
    queryset = Company.objects.filter(discount__active=True)

    if category:
        queryset = queryset.filter(category__id=category)
    top_city = queryset.filter(address__city__id=city).order_by("discount__order_num")
    down_city = queryset.exclude(address__city__id=city).order_by("discount__order_num")
    queryset = chain(top_city, down_city)

    lst = []
    for company in queryset:
        lst.append(CompanyDto(company))
    return lst


class CompanyDetailDto:
    def __init__(self, company):
        self.id = company.id
        self.name = company.name
        self.description = company.description
        self.photo = company.photo
        self.status = company.status
        self.discount = company.discount.percent
        self.rules = company.discount.rules.description
        self.view_count = Looking.objects.get(id=company).counter
        self.longitude = company.address.longitude
        self.lantitude = company.address.latitude
        self.city = company.address.city
        self.address_name = company.address.address_name
        self.social = Social.objects.filter(company=company)


def get_dto_detail_company():
    queryset = Company.objects.all()
    print(queryset)
    lst = []
    for company_detail in queryset:
        lst.append(CompanyDetailDto(company_detail))
    return lst


class ReviewsDto:
    def __init__(self, reviews):
        self.review = reviews.review
        self.customer = reviews.id_customer


def get_dto_reviews():
    queryset = Reviews.objects.all()
    print(queryset)
    list = []
    for review in queryset:
        list.append(ReviewsDto(review))
    return list
