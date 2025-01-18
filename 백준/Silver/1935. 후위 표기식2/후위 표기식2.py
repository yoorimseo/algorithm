N = int(input())
line = input()
nums = [int(input()) for _ in range(N)]
stack = []

for i in line:
    if 'A' <= i <= 'Z':
        stack.append(nums[ord(i) - 65])
    else:
        y = stack.pop()
        x = stack.pop()

        if i == '+':
            stack.append(x + y)
        elif i == '-':
            stack.append(x - y)
        elif i == '*':
            stack.append(x * y)
        elif i == '/':
            stack.append(x / y)

print(f'{stack[0]:.2f}')