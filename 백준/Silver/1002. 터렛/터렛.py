from math import sqrt
T = int(input())

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    diff = abs(r1 - r2)

    ans = 0

    if dist == 0 and r1 == r2:
        ans = -1
    elif dist == r1 + r2 or dist == diff:
        ans = 1
    elif diff < dist < r1 + r2:
        ans = 2

    print(ans)

for _ in range(T):
    solve()