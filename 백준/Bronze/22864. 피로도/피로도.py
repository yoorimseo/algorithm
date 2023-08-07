A, B, C, M = map(int, input().split())
tired = 0
work = 0
hour = 24

if A > M:
    print(0)
else:
    while hour != 0:
        hour -= 1

        if tired + A <= M:
            tired += A
            work += B
        else:
            if tired - C < 0:
                tired = 0
            else:
                tired -= C

    print(work)