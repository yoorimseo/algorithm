import sys
input = sys.stdin.readline

idx = 1
while True:
    cnt = 0
    string = input().rstrip()
    stack = []

    if '-' in string:
        break
    for i in string:
        if i == '{':
            stack.append(i)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            elif not stack:
                cnt += 1
                stack.append('{')

    cnt += len(stack)//2

    print(f'{idx}. {cnt}')
    idx += 1
