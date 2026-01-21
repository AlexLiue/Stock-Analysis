"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_board_concept_cons_em.py
===========================
STOCK_BOARD_CONCEPT_CONS_EM
AKSHARE 东方财富-沪深板块-概念板块-板块成份
"""
from enum import StrEnum


class STOCK_BOARD_CONCEPT_CONS_EM(StrEnum):
    ID = "ID"
    日期 = "日期"
    板块代码 = "板块代码"
    板块名称 = "板块名称"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
