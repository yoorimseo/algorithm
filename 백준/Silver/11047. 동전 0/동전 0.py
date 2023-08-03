N, K = map(int, input().split())
A = []

for i in range(N):
    A.append(int(input()))

A.sort(reverse=True)

res = 0

for j in A:
    if j <= K:
        res += int(K / j)
        K = K % j

print(res)