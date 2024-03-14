N, C = map(int, input().split())
num = list(map(int, input().split()))
res = dict()

for i in num:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)

for key, value in sorted_res:
    for _ in range(value):
        print(key, end=' ')