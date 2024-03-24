## numpy 활용
import numpy as np

a = np.arange(10)
b = np.arange(2, 10)
c = np.arange(1, 10, 2)

print('a = %s'%(a))
print('b = %s'%(b))
print('c = %s'%(c))

a = a.reshape([2, 5])
print('a = %s'%(a))
## reshape는 a.reshape인 이유 = ??
## 객체가 a여서 그런가?



