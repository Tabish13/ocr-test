from django.urls import path

from . import views

urlpatterns = [
    path('', views.PancardActions.as_view(), name='index'),
]