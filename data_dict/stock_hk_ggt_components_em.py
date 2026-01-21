"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_hk_ggt_components_em.py
===========================
STOCK_HK_GGT_COMPONENTS_EM
AKSHARE 港股通成分股
"""
from enum import StrEnum


class STOCK_HK_GGT_COMPONENTS_EM(StrEnum):
    ID = "ID"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    交易所 = "交易所"
    数据日期 = "数据日期"
