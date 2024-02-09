T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    number = sorted(list(set(arr)))
    res = 0
    cnt = 0

    for i in number:
        if arr.count(i) > cnt:
            cnt = arr.count(i)
            res = i
        elif arr.count(i) == cnt:
            if res < i:
                res = i

    print(f'#{N} {res}')