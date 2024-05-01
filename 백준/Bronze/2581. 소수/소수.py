M = int(input())
N = int(input())
res = []

for i in range(M, N+1):
    temp = 0
    if i > 1:
        for j in range(2, i):
            if not i % j:
                temp += 1
                break
        if not temp:
            res.append(i)

if len(res) < 1:
    print(-1)
else:
    print(sum(res))
    print(min(res))