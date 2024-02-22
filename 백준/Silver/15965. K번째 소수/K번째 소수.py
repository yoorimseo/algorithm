BIG_NUM = 10**7
K = int(input())
arr = [1 for _ in range(BIG_NUM+1)]
res = []

for i in range(2, BIG_NUM+1):
    if arr[i]:
        res.append(i)
        for j in range(i+i, BIG_NUM+1, i):
            arr[j] = 0

print(res[K-1])