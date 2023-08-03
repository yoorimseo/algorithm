N = int(input())
M = []

for i in range(N):
    M.append(int(input()))

M.sort(reverse=True)

res = M[0]

for j in range(1, len(M)):
    curr = M[j] * (j + 1)
    if curr > res:
        res = curr

print(res)