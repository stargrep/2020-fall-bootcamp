'''
双均线
'''

window_short = 20
window_long = 120
SD = 0.05

security['short_window'] = np.round(pd.rolling_mean(security['closePrice'], window=window_short), 2)
security['long_window'] = np.round(pd.rolling_mean(security['closePrice'], window=window_long), 2)
security[['closePrice', 'short_window', 'long_window']].tail()