N = int(input())
queue = []

for _ in range(N):
    inp = input().split()
    o = inp[0]

    if o == 'push':
        queue.append(int(inp[1]))
    elif o == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif o == 'size':
        print(len(queue))
    elif o == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif o == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif o == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)