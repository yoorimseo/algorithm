N, K = map(int, input().split())
arr = [True] * (N+1)
arr[0] = arr[1] = False
cnt = 0

for i in range(2, N+1):
    if arr[i]:
        if cnt == K:
            break
        cnt += 1
        P = i
        for j in range(i*2, N+1, i):
            if cnt == K:
                break
            if arr[j]:
                arr[j] = False
                cnt += 1
                P = j
print(P)