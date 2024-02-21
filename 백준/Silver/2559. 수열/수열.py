N, K = map(int, input().split())
arr = list(map(int, input().split()))

acc = []
res = 0
for i in arr:
    res += i
    acc.append(res)

answer = acc[K-1]
for j in range(K, N):
    temp = acc[j] - acc[j-K]
    answer = max(answer, temp)

print(answer)