inp = input()
stack = []
res = 0

for i in range(len(inp)):
    if inp[i] == '(':
        stack.append('(')
    else:
        stack.pop()

        if inp[i-1] == '(':
            res += len(stack)
        else: res += 1

print(res)