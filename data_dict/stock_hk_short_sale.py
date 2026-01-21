"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_hk_short_sale.py
===========================
STOCK_HK_SHORT_SALE
AKSHARE 股票-港股淡仓数据
"""
from enum import StrEnum


class STOCK_HK_SHORT_SALE(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    淡仓股数 = "淡仓股数"
    淡仓金额 = "淡仓金额"
