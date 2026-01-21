"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: find_portfolio_hold_em.py
===========================
FUND_PORTFOLIO_HOLD_EM
AKSHARE 天天基金网-基金档案-投资组合-基金持仓
"""
from enum import StrEnum


class FUND_PORTFOLIO_HOLD_EM(StrEnum):
    ID = "ID"
    基金代码 = "基金代码"
    股票代码 = "股票代码"
    股票名称 = "股票名称"
    占净值比例 = "占净值比例"
    持股数 = "持股数"
    持仓市值 = "持仓市值"
    季报日期 = "季报日期"
