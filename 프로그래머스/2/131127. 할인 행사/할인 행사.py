from collections import Counter

def solution(want, number, discount):
    answer = 0
    product = {w: n for w, n in zip(want, number)}
    sum_num = sum(number)

    for i in range(len(discount) - sum_num + 1):
        if product == Counter(discount[i:i+sum_num]):
            answer += 1
            
    return answer