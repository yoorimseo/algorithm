N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])


res = []

for i in arr:
    cnt = 1

    for j in range(len(arr)):
        if i[0] < arr[j][0] and i[1] < arr[j][1]:
            cnt +=1

    res.append(cnt)

print(*res)