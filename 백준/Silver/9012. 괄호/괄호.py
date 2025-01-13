T = int(input())

for _ in range(T):
    arr = input()
    stack = []

    for i in arr:
        if stack:
            if stack[-1] == '(' and i == ')':
                stack.pop()
                continue
            else:
                stack.append(i)
        else:
            stack.append(i)

    if len(stack):
        print('NO')
    else:
        print('YES')