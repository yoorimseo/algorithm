import re

def findDot(string):
        temp = string
        if string[0] == '.':
            temp = string[1:]
        elif string[-1] == '.':
            temp = string[:len(string)-1]

        return temp

def solution(new_id):
    answer = []

    for i in new_id.lower():
        if 96 < ord(i) < 123:
            answer.append(i)
        elif ord(i) == 45 or ord(i) == 95 or ord(i) == 46:
            answer.append(i)
        elif i.isdigit():
            answer.append(i)

    answer = findDot(re.sub(r'\.+', '.', ''.join(answer)))

    if len(answer) == 0:
        answer = 'a'
    elif 16 <= len(answer):
        answer = answer[:15]

    answer = findDot(answer)

    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
        
    return answer
    