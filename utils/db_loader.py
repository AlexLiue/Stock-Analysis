import re

import pandas as pd

from data_dict import STOCK_ZH_A_HIST_WEEKLY_QFQ
from data_dict.table import TABLE
from utils.tools import get_engine


def load_table(
        table,
        cols,
        where: str = None) -> pd.DataFrame:
    conn = get_engine()
    query_columns = [
        f'"{k}"' if re.search(r"[\u4e00-\u9fa5]", str(k)) else k
        for k in cols
    ]
    query = f"SELECT {', '.join(query_columns)} FROM {table}" if where is None else f"SELECT {', '.join(query_columns)} FROM {table} WHERE {where}"
    return pd.read_sql(query, con=conn)


if __name__ == '__main__':
    stock_basic = load_table(
        table=TABLE.STOCK_ZH_A_HIST_WEEKLY_QFQ,
        cols=[
            STOCK_ZH_A_HIST_WEEKLY_QFQ.日期,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.开盘,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.收盘,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.成交量
        ])
    print(stock_basic)
