import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 주식 수익률 데이터 불러오기
stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name = 'Sheet1')
stock_dt = stock_dt.set_index(['Date']) # date
print(stock_dt)
print()

# 히스토그램 그리기
plt.hist(stock_dt["삼성전자"], histtype = 'step', bins = 10, color = 'red') # step- 선으로 표현, 아무것도 안넣으면 색칠된 토막
plt.hist(stock_dt["코스피200"], bins = 10, color = 'blue') # bins - 나무 도막의 수
plt.show()

# 백분위수 (사분위수)
print(np.percentile(stock_dt["삼성전자"], [0, 25, 50, 75, 100]))
print(np.percentile(stock_dt["코스피200"], [0, 25, 50, 75, 100]))