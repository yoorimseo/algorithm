N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
res = 0

for i in range(N):
    if A[i] > 0:
        A[i] -= B
        res += 1

    if A[i] > 0:
        res += int(A[i] / C)

        if A[i] % C != 0:
            res += 1

print(res)