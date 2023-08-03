change = [500, 100, 50, 10, 5, 1]
N = int(input())
res = 1000 - N
cnt = 0

for i in change:
    cnt += int(res / i)
    res = res % i

    if res == 0:
        break

print(cnt)