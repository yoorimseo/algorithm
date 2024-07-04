def solution(s):
    answer = 0

    for i in range(len(s)):
        stack = []

        for j in range(len(s)):
            if len(stack):
                cmp = stack.pop()
                if (cmp == '(' and s[j] == ')') or (cmp == '{' and s[j] == '}') or (cmp == '[' and s[j] == ']'):
                    continue
                else:
                    stack.append(cmp)
                    stack.append(s[j])
            else:
                stack.append(s[j])

        if len(stack) == 0:
            answer += 1

        s = s[1:] + s[0]

    return answer
