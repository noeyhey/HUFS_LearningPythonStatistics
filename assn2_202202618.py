# (과제 2) 첨부의 stock_daily_return.xlsx 파일에 담긴 엔터테인먼트 4 개사(SM, JYP, YG, HYBE) 의 일별 수익률 자료를 활용하여 다음의 실습을 수행하시오.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

stock_dt = pd.read_excel('stock_daily_return.xlsx', sheet_name='Sheet1')
stock_dt = stock_dt.set_index(['Date'])
print(stock_dt)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 2.1 4개사 수익률 자료의 scatter matrix를 표시하고 간단히 해석하시오.
from pandas.plotting import scatter_matrix
scatter_matrix(stock_dt)
plt.show()

# 2.2 4개사 수익률 자료의 summary statistics와 correlation matrix를 구하여 엑셀파일에 기록하고, correlation matrix에 표시된 결과를 2.1의 결과와 연결하여 간단히 해석하시오.
sum_stat = stock_dt.describe()
corr_matrix = stock_dt.corr()
writer = pd.ExcelWriter('assn2_(2).xlsx', engine = 'xlsxwriter')
sum_stat.to_excel(writer, sheet_name='Sheet1')
corr_matrix.to_excel(writer, sheet_name='Sheet2')
writer.close()

# 2.3 4개사 수익률 자료의 Histogram과 skewness, kurtosis를 구하시오.
plt.hist(stock_dt["SM"], bins = 10, histtype = 'step', color = 'black')
plt.hist(stock_dt["JYP"], bins = 10, histtype = 'step', color = 'red')
plt.hist(stock_dt["YG"], bins = 10, histtype = 'step', color = 'yellow')
plt.hist(stock_dt["HYBE"], bins = 10, histtype = 'step', color = 'blue')
plt.show()

print('SM skew: %0.3f'%(stock_dt["SM"].skew()))
print('SM kurt: %0.3f'%(stock_dt["SM"].kurt()))

print('JYP skew: %0.3f'%(stock_dt["JYP"].skew()))
print('JYP kurt: %0.3f'%(stock_dt["JYP"].kurt()))

print('YG skew: %0.3f'%(stock_dt["YG"].skew()))
print('YG kurt: %0.3f'%(stock_dt["YG"].kurt()))

print('HYBE skew: %0.3f'%(stock_dt["HYBE"].skew()))
print('HYBE kurt: %0.3f'%(stock_dt["HYBE"].kurt()))

# 2.4 4개사 수익률 자료의 boxplot을 표시하고 간단히 해석하시오.
sns.boxplot(data=stock_dt)
plt.show()

# 2.5 4개사 수익률 자료의 correlation heat map을 그리시오.
heatmap = sns.heatmap(stock_dt.corr(), vmin = -1, vmax = 1, annot = True, cmap = 'Reds')
plt.show()