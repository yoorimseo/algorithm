def solution(s):
    answer = [-1]

    for i in range(1, len(s)):
        idx = 0
        for j in range(i, -1, -1):
            if i != j and s[i] == s[j]:
                idx = i - j
                break
        if idx:
            answer.append(idx)
        else:
            answer.append(-1)
            
    return answer