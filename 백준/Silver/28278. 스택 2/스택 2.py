import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    inp = sys.stdin.readline().split()

    if inp[0] == '1':
        stack.append(inp[1])
    elif inp[0] == '2':
        if len(stack):
           print(stack.pop())
        else:
            print(-1)
    elif inp[0] == '3':
        print(len(stack))
    elif inp[0] == '4':
        if len(stack):
            print(0)
        else:
            print(1)
    elif inp[0] == '5':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)