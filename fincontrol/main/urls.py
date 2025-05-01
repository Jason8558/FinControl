from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='MainPage'),
    path('managetransactions', views.transaction_manage, name='TransactionsManage')
]
