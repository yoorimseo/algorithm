N = int(input())
i = 0
cnt = 0

while True:
    if N > i:
        i += 1
        N -= i
        cnt += 1
    else:
        print(cnt)
        break