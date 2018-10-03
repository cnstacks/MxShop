#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxShop 
# Software: PyCharm
# Time    : 2018-10-03 15:55
# File    : views_base.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from django.views.generic.base import View
# from django.views.generic import ListView

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过Django的view实现商品列表;
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     # json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)
        # 方法二：
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        import json
        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        return JsonResponse(json_data, safe=False)
