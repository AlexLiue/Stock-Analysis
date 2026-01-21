"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_yjyg_em.py
===========================
STOCK_YJYG_EM
AKSHARE 东方财富-数据中心-年报季报-业绩预报
"""
from enum import StrEnum


class STOCK_YJYG_EM(StrEnum):
    ID = "ID"
    季报日期 = "季报日期"
    股票代码 = "股票代码"
    股票简称 = "股票简称"
    预测指标 = "预测指标"
    业绩变动 = "业绩变动"
    预测数值 = "预测数值"
    业绩变动幅度 = "业绩变动幅度"
    业绩变动原因 = "业绩变动原因"
    预告类型 = "预告类型"
    上年同期值 = "上年同期值"
    公告日期 = "公告日期"
