N = int(input())
postfix = list(input())
num = [int(input()) for _ in range(N)]
stack = []

for i in postfix:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i) - 65])
    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)

print(f'{stack[0]:.2f}')