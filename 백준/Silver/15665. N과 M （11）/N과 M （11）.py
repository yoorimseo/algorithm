N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def back():
    if len(ans) == M:
        print(*ans)
        return

    check = 0

    for i in arr:
        if check != i:
            ans.append(i)
            check = i
            back()
            ans.pop()

back()