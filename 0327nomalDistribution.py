import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 정규분포
# 정규분포인지 아닌지 판단할 때:
# - 평균, 중앙, 최빈값이 모두 동일해야 함.
# - 각 데이터와 평균과의 차이를 시그마로 나누면 그 변환된 데이터로 구한 분포가 정규분포와 같아야 함.
# 표준정규분포의 이점:
# - 68-95-99.7 법칙 (유의수준)
# 중심극한정리

stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name='Sheet1')
stock_dt = stock_dt.set_index(['Date'])
print(stock_dt)

# 왜도, 첨도 (outlier에 대한 얘기)
# 정규성 -> 왜도가 0이다 (평균값 = 중앙값), 부호를 살려서(세제곱) skewed 방향을 찾음
# 양의 왜도 값을 가진 데이터의 주식, 더 큰 수익률을 가질 확률이 있는 주식
# 반대로 대부분의 주식들이 음의 왜도를 가짐 (금융위기, 코로나 등.)
# 첨도 -> 꼬리에 집중 ! (fat-tailed)
# 3보다 클 때 이상치를 가지고 있음을 의미
print('삼성전자 skew: %0.3f'%(stock_dt["삼성전자"].skew()))
print('삼성전자 kurt: %0.3f'%(stock_dt["삼성전자"].kurt()))

print('SK하이닉스 skew: %0.3f'%(stock_dt["SK하이닉스"].skew()))
print('SK하이닉스 kurt: %0.3f'%(stock_dt["SK하이닉스"].kurt()))

plt.hist(stock_dt["삼성전자"], bins = 10, histtype = 'step', color = 'black')
plt.hist(stock_dt["SK하이닉스"], bins = 10, histtype = 'step', color = 'red')
plt.show()

# seaborn 을 이용한 시각화
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

sns.boxplot(data=stock_dt)
plt.show()

heatmap = sns.heatmap(stock_dt.corr(), vmin = -1, vmax = 1, annot = True, cmap = 'Reds')
plt.show()

# 회전율 = 거래량/상장주식수 -> outlier을 제거하고 분석해야 함. (무언가를 나눴을 때 outlier가 나올 가능성이 높음)
