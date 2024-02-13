import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    inp = sys.stdin.readline().split()

    if inp[0] == 'push':
        queue.append(inp[1])
    elif inp[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif inp[0] == 'size':
        print(len(queue))
    elif inp[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif inp[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif inp[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)