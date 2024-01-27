def solution(num, total):
    sum_num = sum(range(num+1))
    d = total - sum_num
    start = d // num
    answer = [i + start for i in range(1, num+1)]
    
    return answer