from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.CompanyList.as_view()),
    path("company_detail/<int:pk>/", views.CompanyDetail.as_view()),
    path('review/', views.ReviewsCreate.as_view()),
    path('create_cupon/', views.CuponCreate.as_view()),
    path('activate_cupon/', views.ActivateCoupon.as_view()),
    # path("reviews/", views.ReviewsList.as_view()),
]
