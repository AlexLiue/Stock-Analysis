"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_hk_short_sale_em.py
===========================
STOCK_HK_SHORT_SALE_EM
AKSHARE 股票-港股沽空数据-东方财富
"""
from enum import StrEnum


class STOCK_HK_SHORT_SALE_EM(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    最新价 = "最新价"
    沽空股数 = "沽空股数"
    沽空均价 = "沽空均价"
    沽空金额_万 = "沽空金额_万"
    成交金额_万 = "成交金额_万"
    沽空占比 = "沽空占比"
