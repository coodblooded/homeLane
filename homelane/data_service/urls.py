from django.urls import path

from data_service import views
urlpatterns = [
    path('query/', views.BudgetQueryView.as_view(), name='data_query')
]