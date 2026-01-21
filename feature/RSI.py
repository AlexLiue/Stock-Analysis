"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2026/1/21 21:33
# @Author  : PcLiu
# @FileName: RSI.py
===========================

特征计算： RSI-相对强弱指数 (Relative Strength Index)

"""

import vectorbt as vbt

from data_dict import STOCK_ZH_A_HIST_DAILY_HFQ
from data_dict.table import TABLE
from utils.table_loader import load_table


def RSI(df, index='日期', symbol='股票代码', value='收盘', window=14):
    """
    计算 [RSI-相对强弱指数 (Relative Strength Index)](feature/docs/RSI-相对强弱指数 (Relative Strength Index).md)
    :param df: 输入数据
    :param index:  日期列
    :param symbol:  股票代码列（列名）
    :param value:  计算的列值
    :param window: 窗口大小
    :return: RSI 相对强弱指数计算结果
    """

    """ Pivot（透视）：将长格式转为宽格式, 每只股票代码的数据作为一列 """
    wide_df = df.pivot(index=index, columns=symbol, values=value)

    """ 使用 vectorbt 并行计算每只股票的 RSI ,窗口大小 14 """
    rsi = vbt.RSI.run(wide_df, window=window).rsi

    """ 删除 index 索引(窗口大小), levels=0:删除第0层索引, axis=1: 删除列的索引, inplace=True:原地删除 """
    return rsi.vbt.drop_levels(levels=0, axis=1, inplace=True)


if __name__ == '__main__':
    df = load_table(
        table=TABLE.STOCK_ZH_A_HIST_DAILY_HFQ,
        cols=[
            STOCK_ZH_A_HIST_DAILY_HFQ.日期,
            STOCK_ZH_A_HIST_DAILY_HFQ.股票代码,
            STOCK_ZH_A_HIST_DAILY_HFQ.收盘]
    )

    rsi = RSI(df, index='日期', column='股票代码', value='收盘', window=14)

    print(rsi)
