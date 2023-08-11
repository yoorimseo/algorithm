def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        cmp = s[0:i]
        cnt = 1
        string = ''
                
        for j in range(i, len(s), i):
            if cmp == s[j:j + i]:
                cnt += 1
            else:
                string += str(cnt) + cmp if cnt >= 2 else cmp
                cnt = 1
                cmp = s[j:j + i]
        
        string += str(cnt) + cmp if cnt >= 2 else cmp
        answer = min(answer, len(string))
        
    return answer