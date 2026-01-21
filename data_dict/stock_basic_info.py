"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_basic_info.py
===========================
STOCK_BASIC_INFO
AKSHARE 股票基本信息数据
"""
from enum import StrEnum


class STOCK_BASIC_INFO(StrEnum):
    ID = "ID"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    交易所 = "交易所"
    板块 = "板块"
    上市日期 = "上市日期"
    数据日期 = "数据日期"
