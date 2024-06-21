N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def back(start):
    if len(ans) == M:
        print(*ans)
        return

    check = 0

    for i in range(start, N):
        if check != arr[i]:
            ans.append(arr[i])
            check = arr[i]
            back(i)
            ans.pop()

back(0)