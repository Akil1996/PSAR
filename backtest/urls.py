from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.backtest_home, name="backtestHome"),
    path('backtestresult/', views.backtest_result, name="backtestResult"),
]