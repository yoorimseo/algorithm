def solution(arr, divisor):
    answer = sorted(filter(lambda x : x % divisor == 0, arr))
    
    if answer:
        return answer
    
    return [-1]