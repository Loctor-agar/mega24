from itertools import chain

from .models import Company, Category


# def get_filter_city_and_category(query_param):
#     category = query_param.get('category')
#     city = query_param.get('city')
#     queryset = Company.objects.filter(discount__active=True)
#
#     if category:
#         queryset = queryset.filter(category__id=category)
#     top_city = queryset.filter(address__city__id=city).order_by("discount__order_num")
#     down_city = queryset.exclude(address__city__id=city).order_by("discount__order_num")
#     return list(chain(top_city, down_city))
