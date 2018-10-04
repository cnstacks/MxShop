#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MxShop 
# Software: PyCharm
# Time    : 2018-10-03 16:42
# File    : serializers.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ("name", "click_num", "market_price", "add_time")
        fields = "__all__"
