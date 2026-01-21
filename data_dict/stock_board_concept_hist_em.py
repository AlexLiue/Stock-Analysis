"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: stock_board_concept_hist_em.py
===========================
STOCK_BOARD_CONCEPT_HIST_EM
AKSHARE 东方财富-沪深板块-概念板块-历史行情数据
"""
from enum import StrEnum


class STOCK_BOARD_CONCEPT_HIST_EM(StrEnum):
    ID = "ID"
    日期 = "日期"
    板块代码 = "板块代码"
    板块名称 = "板块名称"
    开盘 = "开盘"
    收盘 = "收盘"
    最高 = "最高"
    最低 = "最低"
    涨跌幅 = "涨跌幅"
    涨跌额 = "涨跌额"
    成交量 = "成交量"
    成交额 = "成交额"
    振幅 = "振幅"
    换手率 = "换手率"
