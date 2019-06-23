# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include # 追記7
import debug_toolbar
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), # 追記6
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
