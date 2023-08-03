N = int(input())
P = list(map(int, input().split()))
line = []

for i in range(N):
    line.append([P[i], i + 1])

line.sort()

res = 0

for j in range(N):
    for k in range(j + 1):
        res += line[k][0]

print(res)