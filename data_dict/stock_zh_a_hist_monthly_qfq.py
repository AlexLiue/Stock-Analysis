"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_zh_a_hist_monthly_qfq.py
===========================
STOCK_ZH_A_HIST_MONTHLY_QFQ
沪深京A股月频率数据-前复权
"""
from enum import StrEnum


class STOCK_ZH_A_HIST_MONTHLY_QFQ(StrEnum):
    ID = "ID"
    日期 = "日期"
    股票代码 = "股票代码"
    开盘 = "开盘"
    收盘 = "收盘"
    最高 = "最高"
    最低 = "最低"
    成交量 = "成交量"
    成交额 = "成交额"
    振幅 = "振幅"
    涨跌幅 = "涨跌幅"
    涨跌额 = "涨跌额"
    换手率 = "换手率"
