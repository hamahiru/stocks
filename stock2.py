import numpy as np
from pandas import Series,DataFrame
import pandas as pd
import pandas.io.data as pdweb
import datetime
import matplotlib.pyplot as plt

prices = pdweb.get_data_yahoo(['GOOGL','F','MDT'],start=datetime.datetime(2014,1,1),end=datetime.datetime(2015,8,21))['Adj Close']
prices.tail()
prices_norm = (prices - prices.mean()) / (prices.max() - prices.min())
prices_norm[0]