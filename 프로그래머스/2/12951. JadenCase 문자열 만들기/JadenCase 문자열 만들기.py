def solution(s):
    words = s.split(' ')
    answer = []
    
    for word in words:
        tmp = ''
        
        if word:
            tmp = word[0].upper() + word[1:].lower() 
        
        answer.append(tmp)
        
    return ' '.join(answer)