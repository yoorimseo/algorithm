n = int(input())
w = list(map(int, input().split()))
w.sort(reverse=True)
res = w[0] + w[len(w) - 1]

for i in range(n):
    if w[i] + w[len(w) - (i + 1)] < res:
        res = w[i] + w[len(w) - (i + 1)]

print(res)