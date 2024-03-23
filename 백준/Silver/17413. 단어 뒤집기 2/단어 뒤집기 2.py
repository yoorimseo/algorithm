S = input() + ' '
stack = []
res = ''
state = 0

for i in S:
    if i == '<':
        state = 1
        while len(stack):
            res += stack.pop()

    stack.append(i)

    if i == '>':
        state = 0
        while len(stack):
            res += stack.pop(0)

    if i == ' ' and state == 0:
        stack.pop()
        while len(stack):
            res += stack.pop()
        res += ' '

print(res)