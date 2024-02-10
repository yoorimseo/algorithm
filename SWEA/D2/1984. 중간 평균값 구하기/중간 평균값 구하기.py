T = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    arg = sum(arr) / len(arr)
    print(f'#{i+1} {round(arg)}')