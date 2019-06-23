# -*- coding: utf-8 -*-
# 以下追記8
from django.urls import path
from . import views

# 追記
app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]