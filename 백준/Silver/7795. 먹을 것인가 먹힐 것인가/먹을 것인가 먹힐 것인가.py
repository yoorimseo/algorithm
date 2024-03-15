import bisect

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0

    for a in A:
        cnt += (bisect.bisect(B, a-1))

    print(cnt)