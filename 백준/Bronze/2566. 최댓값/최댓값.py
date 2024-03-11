max_num = 0
x, y = 0, 0

for i in range(1, 10):
    arr = list(map(int, input().split()))

    if max(arr) >= max_num:
        max_num = max(arr)
        x, y = i, arr.index(max(arr))

print(max_num)
print(x, y+1)
