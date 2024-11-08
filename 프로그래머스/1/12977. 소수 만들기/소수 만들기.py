from itertools import combinations

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    arr = list(combinations(nums, 3))
    answer = 0

    for i in arr:
        if is_prime(sum(i)):
            answer += 1
    
    return answer