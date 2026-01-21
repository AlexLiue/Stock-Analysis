"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_szse_area_summary.py
===========================
STOCK_SZSE_AREA_SUMMARY
深圳证券交易所-市场总貌-地区交易排序
"""
from enum import StrEnum


class STOCK_SZSE_AREA_SUMMARY(StrEnum):
    ID = "ID"
    日期 = "日期"
    地区 = "地区"
    总交易额 = "总交易额"
    占市场 = "占市场"
    股票交易额 = "股票交易额"
    基金交易额 = "基金交易额"
    债券交易额 = "债券交易额"
