"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_sse_deal_daily.py
===========================
STOCK_SSE_DEAL_DAILY
上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
"""
from enum import StrEnum


class STOCK_SSE_DEAL_DAILY(StrEnum):
    ID = "ID"
    日期 = "日期"
    板块 = "板块"
    挂牌数 = "挂牌数"
    市价总值 = "市价总值"
    流通市值 = "流通市值"
    成交金额 = "成交金额"
    成交量 = "成交量"
    平均市盈率 = "平均市盈率"
    换手率 = "换手率"
    流通换手率 = "流通换手率"
