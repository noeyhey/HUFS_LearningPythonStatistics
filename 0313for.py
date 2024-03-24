# for 반복문
# 몇 번 반복할 지 알고 있을 때

for i in range(5):
    print(i)

a = ['H', 'e', 'l', 'l', 'o']

for ch in a:
    print(ch)

# while - 조건 반복

i = 0

while i < 5:
    print(i)
    i += 1
    # 무한루프 조심. break 확실히, 혹은 for문 사용

# if 조건문
i = 3

if i > 5:
    print("i>5")
elif i > 0:
    print("positive")
else:
    print("negative")

