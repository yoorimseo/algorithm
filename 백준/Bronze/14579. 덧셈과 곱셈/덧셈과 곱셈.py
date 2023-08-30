a, b = map(int, input().split())
res = 1

for i in range(a, b+1):
    cmp = 0
    for j in range(1, i+1):
        cmp += j

    res *= cmp

print(res % 14579)