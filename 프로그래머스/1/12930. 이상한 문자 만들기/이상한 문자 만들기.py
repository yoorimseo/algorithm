def solution(s):
    answer = []
    
    for word in s.split(' '):
        temp = ''
        
        for idx, w in enumerate(word):
            if idx % 2 == 0 :
                temp += w.upper()
            else:
                temp += w.lower()
                
        answer.append(temp)
        
    return ' '.join(answer)