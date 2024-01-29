N, K = map(int, input().split())
arr = list(range(1, N+1))
idx = 0
res = []

while len(arr) > 0:
    idx += K-1
    idx %= len(arr)
    res.append(arr.pop(idx))

print(f'<{", ".join(map(str, res))}>')