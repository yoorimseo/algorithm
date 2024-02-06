import math

N = int(input())
factorial = str(math.factorial(N))[::-1]
cnt = 0

for i in factorial:
    if i != '0':
        break
    cnt += 1

print(cnt)