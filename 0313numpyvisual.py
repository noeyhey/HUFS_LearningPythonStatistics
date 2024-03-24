import numpy as np
import matplotlib.pyplot as plt

plt.close()

num = 50
low = 0
mid = 10
high = 10

x = np.linspace(1, 50, num)
y1 = np.random.randint(low, high, num)
y2 = np.random.randint(mid, 3*high, num)

plt.plot(x, y1, 'ko')
plt.plot(x, y2, 'bs')

## 색상: b(파랑), g(초록), c(청록), y(노랑), k(검정), w(하양)
## 마커: o, v(역삼각형), ^(삼각형), s(사각형), +, ., --(점선)

plt.legend(('plot1', 'plot2'))
plt.show()