from itertools import combinations

def solution(number):
    arr = list(combinations(number, 3))
    answer = list(filter(lambda x: (sum(x) == 0), arr))
    
    return len(answer)