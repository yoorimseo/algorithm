A, B = map(int, input().split())

cnt = 0
flag = False
arr = []

for i in range(1, B+1):
    for j in range(i):
        arr.append(i)
        cnt += 1

        if cnt == B:
            flag = True
            break

    if flag:
        break

print(sum(arr[A-1:B]))