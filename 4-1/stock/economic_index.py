import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr


USD_KRX = fdr.DataReader('USD/KRW',start='2019-01-01')
graph = USD_KRX.loc[:,'Close'].plot()
graph.axhline(1050, ls ='--', color ='r')
graph.axhline(1150,ls='--',color = 'r')
print(USD_KRX.loc[:,'Close'])