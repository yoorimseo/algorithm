N = int(input())
arr = list(map(int, input().split()))
res = []
tmp = 0

for i in arr:
    if i:
        tmp += i
        res.append(tmp)
    else:
        tmp = 0

print(sum(res))