N = int(input())
A = list(map(int, input().split()))
d = [0] * N

d[0] = A[0]

for i in range(1, N):
    d[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + A[i])

print(max(d))