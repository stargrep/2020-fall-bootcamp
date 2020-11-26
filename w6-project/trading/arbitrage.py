'''
https://www.zhihu.com/question/38359735/answer/950688523
例子，证明两个symbol是否存在协整性: binance的BTC/USDT 和 binance的ETH/USDT one year
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from vitu import api

data1 = api.coinbar(symbol='BTCUSDT',exchange='binance',freq='daily',start_date='2019-01-01',end_date='2019-12-01')['close']
data1 = data1.reset_index(drop=True)
data1.columns = ['binance.btcusdt']
data1.plot(figsize=(20,8))
plt.show()


from statsmodels.tsa.stattools import adfuller,coint

def testStationarity(data):
    adftest = adfuller(data)
    result = pd.Series(adftest[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])
    for key,value in list(adftest)[4].items():
        result['Critical Value (%s)'%key] = value
    return result

x=np.array(data1)
y=np.array(data2)
zz=pd.concat([testStationarity(x),testStationarity(y)],axis=1)
zz.columns=['binance.btcusdt','binance.ethusdt']

diffx=data1.diff(1)
diffx.dropna(inplace=True)
diffx=np.array(diffx)
diffy=data2.diff(1)
diffy.dropna(inplace=True)
diffy=np.array(diffy)
tz=pd.concat([testStationarity(diffx),testStationarity(diffy)],axis=1)
zz.columns=['binance.btcusdt','binance.ethusdt']

mean=(data1-data2).mean()
std=(data1-data2).std()

s1=pd.Series(mean,index=range(len(data1)))
s2=pd.Series(mean+std,index=range(len(data1)))
s3=pd.Series(mean-std,index=range(len(data1)))

data3=pd.concat([data1-data2,s1,s2,s3],axis=1)
data3.columns=['spreadprice','mean','upper','down']
data3.plot(figsize=(14,7))
print(mean+std,mean-std)
plt.grid()
plt.show()

