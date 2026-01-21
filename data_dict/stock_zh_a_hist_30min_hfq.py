"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_zh_a_hist_30min_hfq.py
===========================
STOCK_ZH_A_HIST_30MIN_HFQ
沪深京A股30分频数据-后复权
"""
from enum import StrEnum


class STOCK_ZH_A_HIST_30MIN_HFQ(StrEnum):
    ID = "ID"
    时间 = "时间"
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
