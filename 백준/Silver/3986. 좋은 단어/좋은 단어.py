N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    stack = []

    for i in word:
        if len(stack):
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if len(stack) == 0:
        cnt += 1

print(cnt)