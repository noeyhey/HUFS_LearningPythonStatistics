import pandas as pd
import matplotlib.pyplot as plt

stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name='Sheet1')
stock_dt = stock_dt.set_index(['Date'])

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# scatter -> 모양 방향 강도
plt.scatter(stock_dt["삼성전자"], stock_dt["코스피200"])
plt.xlabel('삼성전자')
plt.ylabel('코스피200')


# scatter matrix
from pandas.plotting import scatter_matrix
scatter_matrix(stock_dt)
plt.show()


# 요약통계량 - 보고서에 올릴 데이터에 대한 통계치를 포맷화할 때 사용
stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name='Sheet1')
stock_dt = stock_dt.set_index(['Date'])

sum_stat = stock_dt.describe()
print(sum_stat)
print()
corr_matrix = stock_dt.corr()
print(corr_matrix)


# 엑셀로 내보내서 파일로 만들기
writer = pd.ExcelWriter('summary_statistics.xlsx', engine = 'xlsxwriter')
sum_stat.to_excel(writer, sheet_name='Sheet1')
corr_matrix.to_excel(writer, sheet_name='Sheet2')
writer.close()
