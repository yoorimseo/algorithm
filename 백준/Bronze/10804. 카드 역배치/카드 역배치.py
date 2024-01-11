arr = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    temp = arr[a - 1:b]
    temp.reverse()
    arr = arr[:a - 1] + temp + arr[b:]

print(*arr)