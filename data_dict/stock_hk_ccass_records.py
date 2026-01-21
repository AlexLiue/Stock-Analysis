"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_hk_ccass_records.py
===========================
STOCK_HK_CCASS_RECORDS
AKSHARE 股票-香港中央结算系統持股记录
"""
from enum import StrEnum


class STOCK_HK_CCASS_RECORDS(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    机构编号 = "机构编号"
    机构名称 = "机构名称"
    持股量 = "持股量"
    百分比 = "百分比"
