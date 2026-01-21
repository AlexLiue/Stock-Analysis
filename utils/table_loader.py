import re

import pandas as pd

from data_dict import STOCK_ZH_A_HIST_WEEKLY_QFQ
from data_dict.table import TABLE
from utils.config import get_cfg
from utils.logger import get_logger
from utils.tools import get_engine



def load_table(
        table,
        cols,
        where: str = None,
        order: str = None) -> pd.DataFrame:
    logger = get_logger("table_loader", get_cfg()["analysis-logging"]["filename"])
    conn = get_engine()
    query_columns = [
        f'"{k}"' if re.search(r"[\u4e00-\u9fa5]", str(k)) else k
        for k in cols
    ]
    query = f"SELECT {', '.join(query_columns)} FROM {table}"
    if where is not None:
        query = query + F" WHERE {where}"
    if order is not None:
        query = query + F" ORDER BY {order}"

    logger.info(f"Load Table [{table}] With SQL [{query}]")
    return pd.read_sql(query, con=conn)


if __name__ == '__main__':
    stock_basic = load_table(
        table=TABLE.STOCK_ZH_A_HIST_WEEKLY_QFQ,
        cols=[
            STOCK_ZH_A_HIST_WEEKLY_QFQ.日期,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.开盘,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.收盘,
            STOCK_ZH_A_HIST_WEEKLY_QFQ.成交量
        ],
        where=None,
        order= STOCK_ZH_A_HIST_WEEKLY_QFQ.日期 + " ASC"
    )
    print(stock_basic)
