from django.urls import path

from query_service import views
urlpatterns = [
    path('budget/', views.BudgetHomeView.as_view(), name='budget'),
    path('sqft/', views.HomeSqftView.as_view(), name='sqft'),
    path('year/', views.HomeYearView.as_view(), name='year')
]