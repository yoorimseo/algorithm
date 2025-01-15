import sys

left = list(input())
right = []
M = int(input())

for _ in range(M):
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

res = left + right[::-1]
print(''.join(res))