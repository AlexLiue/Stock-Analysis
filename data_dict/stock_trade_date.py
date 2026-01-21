"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_trade_date.py
===========================
STOCK_TRADE_DATE
AKSHARE 证券交易所-交易日历
"""
from enum import StrEnum


class STOCK_TRADE_DATE(StrEnum):
    ID = "ID"
    交易所 = "交易所"
    交易日期 = "交易日期"
    数据日期 = "数据日期"
