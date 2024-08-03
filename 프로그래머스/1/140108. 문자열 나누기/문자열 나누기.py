def solution(s):
    answer = 0

    while s:
        x = s[0]
        same, diff = 0, 0

        for i in range(len(s)):
            if s[i] == x:
                same += 1
            else:
                diff += 1

            if same == diff:
                answer += 1
                s = s[i+1:]
                break
        else:
            answer += 1
            break

    return answer
