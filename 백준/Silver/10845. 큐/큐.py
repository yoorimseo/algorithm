from collections import deque

N = int(input())
arr = deque()

for _ in range(N):
    inp = input().split()

    if inp[0] == 'push':
        arr.append(int(inp[1]))
    elif inp[0] == 'pop':
        print(arr.popleft()) if arr else print(-1)
    elif inp[0] == 'size':
        print(len(arr))
    elif inp[0] == 'empty':
        print(0) if arr else print(1)
    elif inp[0] == 'front':
        print(arr[0]) if arr else print(-1)
    elif inp[0] == 'back':
        print(arr[-1]) if arr else print(-1)