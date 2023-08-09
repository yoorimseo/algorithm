import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    arr.sort()

    cnt = 1
    cmp = arr[0][1]

    for i in range(1, N):
        if cmp > arr[i][1]:
            cnt += 1
            cmp = arr[i][1]

    print(cnt)