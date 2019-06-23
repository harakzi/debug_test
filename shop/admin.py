from django.contrib import admin

# DB情報取込のためのインポート
from .models import Good


# adminメソッドでGoods登録
admin.site.register(Good)