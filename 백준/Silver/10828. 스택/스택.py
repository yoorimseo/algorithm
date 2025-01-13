N = int(input())
stack = []

for _ in range(N):
    inp = input().split()
    o = inp[0]

    if len(inp) > 1:
        if o == 'push':
            stack.append(int(inp[1]))
    else:
        if  o == 'pop':
            if stack: print(stack.pop())
            else: print(-1)
        elif o == 'size':
            print(len(stack))
        elif o == 'empty':
            if stack: print(0)
            else: print(1)
        elif o == 'top':
            if stack: print(stack[-1])
            else: print(-1)