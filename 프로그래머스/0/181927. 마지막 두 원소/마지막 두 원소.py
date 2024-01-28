def solution(num_list):
    answer = num_list
    n = 0
    if num_list[-1] > num_list[-2]:
        n = num_list[-1] - num_list[-2]
    else:
        n = num_list[-1] * 2
    answer.append(n)
    
    return answer