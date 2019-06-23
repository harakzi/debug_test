# -*- coding: utf-8 -*-
from django import forms


class GoodSearchForm(forms.Form):

    title = forms.CharField(
            initial = '',
            label = '商品名',
            required = False,
        )

    price = forms.IntegerField(
            initial = '',
            label = '値段',
            required = False,
        )


