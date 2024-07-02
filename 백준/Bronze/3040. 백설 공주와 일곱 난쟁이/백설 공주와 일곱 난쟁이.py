arr = sorted([int(input()) for _ in range(9)])
res = 0

for i in range(8):
    if res:
        break

    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            arr.pop(j)
            arr.pop(i)
            res = 1
            break

print(*arr, sep='\n')