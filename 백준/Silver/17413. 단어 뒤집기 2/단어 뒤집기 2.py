S = input() + ' '
stack = []
res = ''
flag = 0

for i in S:
    if i == '<':
        flag = 1
        while len(stack):
            res += stack.pop()
    
    stack.append(i)

    if i == '>':
        flag = 0
        while len(stack):
            res += stack.pop(0)

    if i == ' ' and flag == 0:
        stack.pop()
        while len(stack):
            res += stack.pop()
        res += ' '

print(res)