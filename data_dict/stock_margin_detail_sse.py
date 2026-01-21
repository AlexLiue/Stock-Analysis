"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_margin_detail_sse.py
===========================
STOCK_MARGIN_DETAIL_SSE
AKSHARE 上海证券交易所-融资融券数据-融资融券汇总数据
"""
from enum import StrEnum


class STOCK_MARGIN_DETAIL_SSE(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    融资余额 = "融资余额"
    融资买入额 = "融资买入额"
    融资偿还额 = "融资偿还额"
    融券余量 = "融券余量"
    融券卖出量 = "融券卖出量"
    融券偿还量 = "融券偿还量"
