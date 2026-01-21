"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_board_industry_name_em.py
===========================
STOCK_BOARD_INDUSTRY_NAME_EM
AKSHARE 东方财富网-行情中心-沪深京板块-行业板块
"""
from enum import StrEnum


class STOCK_BOARD_INDUSTRY_NAME_EM(StrEnum):
    ID = "ID"
    日期 = "日期"
    排名 = "排名"
    板块名称 = "板块名称"
    板块代码 = "板块代码"
    最新价 = "最新价"
    涨跌额 = "涨跌额"
    涨跌幅 = "涨跌幅"
    总市值 = "总市值"
    换手率 = "换手率"
    上涨家数 = "上涨家数"
    下跌家数 = "下跌家数"
    领涨股票 = "领涨股票"
    领涨股票_涨跌幅 = "领涨股票_涨跌幅"
