A, B = map(int, input().split())
cnt = 1

while B != A:
    cnt += 1
    tmp = B

    if B == A:
        break

    if B % 10 == 1:
        B = B // 10
    elif B % 2 == 0:
        B = B // 2

    if tmp == B:
        cnt = -1
        break

print(cnt)