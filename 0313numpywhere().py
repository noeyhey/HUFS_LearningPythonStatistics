import numpy as np

a = np.linspace(1, 50, 50)
print(a)
print()

find = np.where(a == 25)
print(find) # 주소를 찍어라
print(a[find]) # 주소의 값을 찍어라
