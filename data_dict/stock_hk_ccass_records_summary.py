"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_hk_ccass_records_summary.py
===========================
STOCK_HK_CCASS_RECORDS_SUMMARY
AKSHARE 股票-香港中央结算系統持股记录-汇总
"""
from enum import StrEnum


class STOCK_HK_CCASS_RECORDS_SUMMARY(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    持股类型 = "持股类型"
    持股量 = "持股量"
    参数者数 = "参数者数"
    百分比 = "百分比"
