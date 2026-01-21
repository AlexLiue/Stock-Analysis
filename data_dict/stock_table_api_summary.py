"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_table_api_summary.py
===========================
STOCK_TABLE_API_SUMMARY
AKSHARE 股票接口API信息数据
"""
from enum import StrEnum


class STOCK_TABLE_API_SUMMARY(StrEnum):
    ID = "ID"
    接口 = "接口"
    地址 = "地址"
    描述 = "描述"
    备注 = "备注"
    数据日期 = "数据日期"
