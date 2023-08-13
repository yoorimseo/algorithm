N = int(input())
arr = ['*' for _ in range(N)]
cnt = 0

for _ in range(N):
    num, location = map(int, input().split())

    if arr[num - 1] == '*':
        arr[num - 1] = location
    elif arr[num - 1] != location:
        cnt += 1
        arr[num - 1] = location
        
print(cnt)