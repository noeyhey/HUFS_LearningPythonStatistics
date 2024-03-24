import numpy as np
import pandas as pd

sample_array = np.array([1, 2, 3, 4, 5])

sample_df = pd.DataFrame({
    'col1': sample_array,
    'col2': sample_array*2,
    'col3': ["A", "B", "C", "D", "E"]
})

# column 이름, row 이름 설정 가능
# 하지만 row 이름 관리가 힘듦.

print(sample_df)

## dataframe 병합

df_1 = pd.DataFrame({
    'col1': np.array([1, 2, 3]),
    'col2': np.array(["A", "B", "C"])
})
df_2 = pd.DataFrame({
    'col1': np.array([4, 5, 6]),
    'col2': np.array(["D", "E", "F"])
})

print(df_1)
print(df_2)

print(pd.concat([df_1, df_2]))
print(pd.concat([df_1, df_2], axis = 1))

## df1 = 2001~2010, df2 = 2011~2020 -> axis = 0
## df1 = Asia country, df2 = Europe country -> axis = 1



print("")
print("열에 대한 작업")


print(sample_df.col2)
print(sample_df["col2"])
print(sample_df[["col2", "col3"]])
print(sample_df.drop("col1", axis = 1))

# print(sample_df["col2", "col3"]) #왜 오류가 날까?

print("행에 대한 작업")

print(sample_df)
print(sample_df.head(n=3))
print(sample_df.query('index==0'))

print("") # 어떤 값을 호출하고 싶을 때
print(sample_df)
print(sample_df.query('col3 == "A"'))
print(sample_df.query('col3 == "A" | col3 == "D"')) # | = or
print(sample_df.query('col3 == "A" & col1 == "3"')) # & = and  --> empty dataframe
print(sample_df.query('col3 == "A"')[["col2", "col3"]])
