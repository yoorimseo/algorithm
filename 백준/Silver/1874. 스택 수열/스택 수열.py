curr = 1
temp = True
stack = []
op = []

N = int(input())

for _ in range(N):
    num = int(input())
    
    while curr <= num:
        stack.append(curr)
        op.append('+')
        curr += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp:
    print(*op, sep='\n')
else:
    print("NO")