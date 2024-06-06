P = int(input())

for _ in range(P):
    inp = list(map(int, input().split()))
    T = inp[0]
    arr = inp[1:]
    cnt = 0

    for i in range(20):
        for j in range(20-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(T, cnt)