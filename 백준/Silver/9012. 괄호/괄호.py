T = int(input())

for _ in range(T):
    stack = []
    inp = list(input())

    for i in inp:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    print('NO') if stack else print('YES')