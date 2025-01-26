def solution(phone_number):
    answer = ''
    phone_number = phone_number[::-1]
    
    for i in range(len(phone_number)):
        if i > 3:
            answer += '*'
        else:
            answer += phone_number[i]
    
    return answer[::-1]