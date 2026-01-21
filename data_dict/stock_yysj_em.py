"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_yysj_em.py
===========================
STOCK_YYSJ_EM
AKSHARE 东方财富-数据中心-年报季报-预约披露时间
"""
from enum import StrEnum


class STOCK_YYSJ_EM(StrEnum):
    ID = "ID"
    季报日期 = "季报日期"
    股票代码 = "股票代码"
    股票简称 = "股票简称"
    首次预约时间 = "首次预约时间"
    一次变更日期 = "一次变更日期"
    二次变更日期 = "二次变更日期"
    三次变更日期 = "三次变更日期"
    实际披露时间 = "实际披露时间"
