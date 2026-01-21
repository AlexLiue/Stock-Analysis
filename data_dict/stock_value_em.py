"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_value_em.py
===========================
STOCK_VALUE_EM
AKSHARE 东方财富网-数据中心-估值分析-每日互动-每日互动-估值分析
"""
from enum import StrEnum


class STOCK_VALUE_EM(StrEnum):
    ID = "ID"
    日期 = "日期"
    证券代码 = "证券代码"
    证券简称 = "证券简称"
    交易所 = "交易所"
    板块代码 = "板块代码"
    板块名称 = "板块名称"
    总市值 = "总市值"
    流通市值 = "流通市值"
    当日收盘价 = "当日收盘价"
    当日涨跌幅 = "当日涨跌幅"
    总股本 = "总股本"
    流通股本 = "流通股本"
    市盈率TTM = "市盈率TTM"
    市盈率LAR = "市盈率LAR"
    市净率 = "市净率"
    市现率TTM = "市现率TTM"
    市现率LAR = "市现率LAR"
    市销率TTM = "市销率TTM"
    市盈增长比 = "市盈增长比"
