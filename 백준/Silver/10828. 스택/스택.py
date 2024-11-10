N = int(input())
stack = []

for _ in range(N):
    inp = input().split()

    if inp[0] == 'push':
        stack.append(inp[1])
    elif inp[0] == 'top':
        print(stack[-1]) if stack else print(-1)
    elif inp[0] == 'empty':
        print(0) if stack else print(1)
    elif inp[0] == 'size':
        print(len(stack))
    elif inp[0] == 'pop':
        print(stack.pop()) if stack else print(-1)