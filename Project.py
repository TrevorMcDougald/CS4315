# #  NumPy and Pandas imports
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame
#
# #  Reading time series
# from pandas_datareader import data
#
# #  Time stamps
# import datetime as datetime
#
# #  Visualization (sns is a visualization library based on matplotlib)
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('darkgrid')
#
# #################################################
#
# #  Stock tickers to retrieve historical index data
# ticker_index_data = ['AMD', 'CSCO']
#
# #  Assign a database with historical stock quotes from Yahoo! Finance to each ticker
# for ticker in ticker_index_data:
#     globals()[ticker] = data.get_data_yahoo(ticker, '2017-10-10', '2019-04-10')
#                                                     #  Changed start to 1.5 years
# #  Display the five most recent results
# print(AMD.tail())
#
# ################################################
#
# AMD.describe()
#
# x = 3
