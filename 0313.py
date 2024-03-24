## formatting
#### %f : 실수로 데이터 처리 %(변수) , %d: 정수, %s: 문자
a = 2
b = a+1
c = 4/3
d = a*3
e = b**3
f = 4%3

print('a=%f\n b=%f\n c=%f\n d=%f\n e=%f\n f=%f\n' %(a, b, c, d, e, f))


## list 자료형
c = [1, 2, 3]
length = len(c)
print('c[0], c[1], c[2]) = %d %d %d'%(c[0], c[1], c[2]))
print('length = %d\n'%(length))

# c=[[1, 2], [3, 4]]
c=[[1, 2], [3, 4], [5, 6]]
length = len(c)
# print('c[0][0], c[0][1], c[1][0], c[1][1]) = %d %d %d %d'%(c[0][0], c[0][1], c[1][0], c[1][1]))
print('length = %d'%(length))

## length = 2인 이유 -> [5, 6]을 추가했을 때 length가 3으로 변함
## m x n matrix