#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxShop 
# Software: PyCharm
# Time    : 2018-10-04 11:31
# File    : filter.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类;
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max',]
