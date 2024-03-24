# [과제1] 주식수익률의 평균, 분산, 상관계수
# 주어진 수익률 자료(stock_monthly_return)를 이용하여 다음 과제를 수행하시오.
import pandas as pd
import numpy as np

stock_dt = pd.read_excel('stock_monthly_return.xlsx', sheet_name = 'Sheet1')
stock_dt = stock_dt.set_index(['Date'])

sse_ret = stock_dt["삼성전자"]
skHinix_ret = stock_dt["SK하이닉스"]
meritz_ret = stock_dt["메리츠금융지주"]
k200_ret = stock_dt["코스피200"]

# 1.1 개별 3종목과 시장지수의 월평균 수익률을 구하고 결과를 비교하시오.
sse_mean = np.mean(sse_ret)
skHinix_mean = np.mean(skHinix_ret)
meritz_mean = np.mean(meritz_ret)
k200_mean = np.mean(k200_ret)

print('sse_mean =', sse_mean)
print('skHinix_mean =', skHinix_mean)
print('meritz_mean =', meritz_mean)
print('k200_mean =', k200_mean)
print()

# 1.2 개별 3종목과 시장지수의 월수익률의 분산과 표준편차를 구하고 결과를 비교하시오.
sse_var = np.var(sse_ret)
sse_std = np.std(sse_ret)
skHinix_var = np.var(skHinix_ret)
skHinix_std = np.std(skHinix_ret)
meritz_var = np.var(meritz_ret)
meritz_std = np.std(meritz_ret)
k200_var = np.var(k200_ret)
k200_std = np.std(k200_ret)

print('sse_var =', sse_var)
print('sse_std =', sse_std)
print('skHinix_var =', skHinix_var)
print('skHinix_std =', skHinix_std)
print('meritz_var =', meritz_var)
print('meritz_std =', meritz_std)
print('k200_var =', k200_var)
print('k200_std =', k200_std)
print()


# 1.3 삼성전자 - SK하이닉스, 삼성전자 - 메리츠금융지주의 상관계수를 각각 구하고 결과를 비교하시오.
# (삼성전자와 SK 하이닉스는 같은 산업, 메리츠금융지주는 다른 산업.)

sse_skHinix_corr = np.corrcoef(sse_ret, skHinix_ret)
see_meritz_corr = np.corrcoef(sse_ret, meritz_ret)

print('sse_skHinix_corr =', sse_skHinix_corr)
print('sse_meritz_corr =', see_meritz_corr)