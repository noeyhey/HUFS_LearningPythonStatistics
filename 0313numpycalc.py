import numpy as np

a = np.array([[1, 2], [3, 4]])
b = a + 3

print('a = %s\n'%a)
print('b = %s\n'%b)

## 상수와 행렬의 곱

c = np.dot(a, b) ## 내적
d = np.multiply(a, b) ## 행렬의 곱
e = a * b ## 행렬의 곱
f = np.transpose(a) ## 전치행렬
g = np.linalg.inv(a) ## 역행렬

print('c = %s\n'%c)
print('d = %s\n'%d)
print('e = %s\n'%e)
print('f = %s\n'%f)
print('g = %s\n'%g)