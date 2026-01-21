"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_margin_szse.py
===========================
STOCK_MARGIN_SZSE
AKSHARE 深证证券交易所-融资融券数据-融资融券交易明细数据
"""
from enum import StrEnum


class STOCK_MARGIN_SZSE(StrEnum):
    ID = "ID"
    日期 = "日期"
    融资买入额 = "融资买入额"
    融资余额 = "融资余额"
    融券卖出量 = "融券卖出量"
    融券余量 = "融券余量"
    融券余额 = "融券余额"
    融资融券余额 = "融资融券余额"
