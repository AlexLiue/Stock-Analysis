"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: fund_name_em.py
===========================
FUND_NAME_EM
AKSHARE 东方财富网-天天基金网-基金数据-所有基金的基本信息数据
"""
from enum import StrEnum


class FUND_NAME_EM(StrEnum):
    ID = "ID"
    基金代码 = "基金代码"
    拼音缩写 = "拼音缩写"
    基金简称 = "基金简称"
    基金类型 = "基金类型"
    拼音全称 = "拼音全称"
    导入日期 = "导入日期"
    最新持仓日期 = "最新持仓日期"
