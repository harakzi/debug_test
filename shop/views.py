# -*- coding: utf-8 -*-
# 以下追記9→次はmodels編集
from django.views import generic

from .models import Good
from .forms import GoodSearchForm
from django.db.models import Q


class IndexView(generic.ListView):

    paginate_by = 5
    template_name = 'shop/index.html'
    model = Good


    def post(self, request, *args, **kwargs):

        form_value = [
                self.request.POST.get('title', None),
                self.request.POST.get('price', None),
            ]


        request.session['form_value'] = form_value

        # 不明
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()

        # generic/list.pyのget()メソッドが呼び出される
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        title = ''
        price = ''

        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            price = form_value[1]

        #import pdb; pdb.set_trace()
        default_data = {'title' : title, 'price' : price}

        # やや不明（どうやってディクショナリのkeyをフォームのtitle, priceに振り分けているのか）
        test_form = GoodSearchForm(initial = default_data)

        context['test_form'] = test_form
        return context


    def get_queryset(self): # 呼び出された（オーバーライドされたメソッド）

        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            price = form_value[1]

            condition_title = Q()
            condition_price = Q()

            if len(title) != 0 and title[0]:
                condition_title = Q(title__contains = title)
            if len(price) != 0 and price[0]:
                condition_price = Q(price__contains = price)

            return Good.objects.select_related().filter(condition_title & condition_price)

        else:
            return Good.objects.none()

