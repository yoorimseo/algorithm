N, M = map(int, input().split())
arr = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    swap = list(reversed(arr[i-1:j]))

    for n in swap:
        if i-1 < j:
            arr[i-1] = n
            i += 1

print(*arr)