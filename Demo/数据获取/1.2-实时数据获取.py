# pip install akshare --upgrade
# pip install efinance --upgrade
# pip install qstock -–upgrade
# TuShare  https://tushare.pro/document/1       https://tushare.pro/document/2
# AKShare  https://akshare.akfamily.xyz/introduction.html      https://akshare.akfamily.xyz/data/index.html
# Efinance https://github.com/Micro-sheep/efinance      https://efinance.readthedocs.io/en/latest/
# Qstock https://pypi.org/project/qstock/
import tushare as ts
import akshare as ak
import efinance as ef
import qstock as qs
import pandas as pd

# 设置显示的最大列数
pd.set_option('display.max_columns', None)
# 设置显示的最大行数
pd.set_option('display.max_rows', None)
# 设置显示每列的最大宽度
pd.set_option('display.max_colwidth', None)
# 设置显示小数的精度
pd.set_option('display.precision', 2)
# 设置是否显示科学计数法
pd.set_option('display.float_format', '{:.2f}'.format)


# 一、获取实时数据（日、周、月）
def get_stock_realtime_data(source='', code=''):
    if source == 'tushare':
        df = ts.get_realtime_quotes(code) # df = ts.realtime_quote(ts_code="000651.SZ")
        return df
    elif source == 'akshare':
        # df = ak.stock_zh_a_spot_em()
        # df = ak.stock_zh_a_hist_min_em(symbol=code, start_date='2023-05-04 10:30:00', end_date='2023-06-02 15:00:00',
        #                                period='30')
        df = ak.stock_zh_a_hist_min_em(symbol=code, period='30') # 不加日期则实时输出
        return df
    elif source == 'efinance':
        # df1 = ef.stock.get_latest_quote(code)
        # df2 = ef.stock.get_latest_quote(stock_codes=[code, '600519'])
        df = ef.stock.get_quote_history(stock_codes=code, beg='20230504', end='20230602', klt='30')
        return df
    elif source == 'qstock':
        # df1 = qs.realtime_data(code=code)
        df2 = qs.realtime_data(code=[code, '600519', '锂电池ETF']) # 可以股票、板块混传
        return df2
    else:
        raise ValueError('不支持的数据源，请输入正确的数据源名称。')


# print(get_stock_realtime_data(source='tushare', code='000651'))
print(get_stock_realtime_data(source='akshare', code='000651'))
# print(get_stock_realtime_data(source='efinance', code='000651'))
# print(get_stock_realtime_data(source='qstock', code='000651'))
