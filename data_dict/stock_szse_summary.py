"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_szse_summary.py
===========================
STOCK_SZSE_SUMMARY
深圳证券交易所-市场总貌-证券类别统计
"""
from enum import StrEnum


class STOCK_SZSE_SUMMARY(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券类别 = "证券类别"
    数量 = "数量"
    成交金额 = "成交金额"
    总市值 = "总市值"
    流通市值 = "流通市值"
