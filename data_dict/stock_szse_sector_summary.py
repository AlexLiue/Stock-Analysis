"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_szse_sector_summary.py
===========================
STOCK_SZSE_SECTOR_SUMMARY
深圳证券交易所-统计资料-股票行业成交数据
"""
from enum import StrEnum


class STOCK_SZSE_SECTOR_SUMMARY(StrEnum):
    ID = "ID"
    日期 = "日期"
    名称 = "名称"
    名称英文 = "名称英文"
    交易天数 = "交易天数"
    成交金额 = "成交金额"
    成交金额占比 = "成交金额占比"
    成交股数 = "成交股数"
    成交股数占比 = "成交股数占比"
    交笔数 = "交笔数"
    成交笔数占比 = "成交笔数占比"
