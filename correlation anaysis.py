import pandas as pd
import numpy as np

stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name = 'Sheet1')
stock_dt = stock_dt.set_index(['Date'])

sse_ret = stock_dt["삼성전자"] # SamsungElectronic_return
k200_ret = stock_dt["코스피200"]

cov = np.cov(sse_ret, k200_ret, ddof = 1)
print(cov)
print('삼성전자-k200 공분산 = %.3f' %(cov[0, 1]))
# 분산의 개념을 서로 다른 개체의 분산 간의 관계로 묻는 것 = 공분산
# 단위가 살아 있음 (cm, m, $ 등등) -> 단위를 없애주는 상관계수 (비교 가능)

print() # 상관계수 = (공분산) / (각각의 표준편차) -> 표준화한 수치 (-1 ~ 1 사이의 값을 가짐)
corr = np.corrcoef(sse_ret, k200_ret) # 자유도 조정이 없는 이유 -> 분자 분모에 모두 존재, 약분 되어서 필요 X
print(corr)
print('삼성전자-k200 상관계수 = %.3f' %(corr[0, 1]))
