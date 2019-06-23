# -*- coding: utf-8 -*-
# 以下追記10→次はforms定義
from django.db import models

class Good(models.Model):
    # 商品テーブル

    class Meta:
        db_table = 'good'

    title = models.CharField(verbose_name='商品名' ,max_length=255)
    price = models.IntegerField(verbose_name='値段', null = True, blank=True)

    def __str__(self):
        return self.title
