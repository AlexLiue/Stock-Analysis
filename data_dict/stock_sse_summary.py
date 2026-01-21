"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_sse_summary.py
===========================
STOCK_SSE_SUMMARY
A股-股票市场总貌-上海证券交易所
"""
from enum import StrEnum


class STOCK_SSE_SUMMARY(StrEnum):
    ID = "ID"
    日期 = "日期"
    项目 = "项目"
    上市股票 = "上市股票"
    总股本 = "总股本"
    流通股本 = "流通股本"
    总市值 = "总市值"
    流通市值 = "流通市值"
    平均市盈率 = "平均市盈率"
