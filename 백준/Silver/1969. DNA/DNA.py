N, M = map(int, input().strip().split())
DNA = [input().strip() for i in range(N)]
res = ''
cnt = 0

for m in range(M):
    arr = [0, 0, 0, 0] # A, C, G, T

    for n in range(N):
        if DNA[n][m] == 'A':
            arr[0] += 1
        elif DNA[n][m] == 'C':
            arr[1] += 1
        elif DNA[n][m] == 'G':
            arr[2] += 1
        elif DNA[n][m] == 'T':
            arr[3] += 1

    max_idx = arr.index(max(arr))

    if max_idx == 0:
        res += 'A'
    elif max_idx == 1:
        res += 'C'
    elif max_idx == 2:
        res += 'G'
    elif max_idx == 3:
        res += 'T'

    cnt += sum(arr) - max(arr)

print(res)
print(cnt)
