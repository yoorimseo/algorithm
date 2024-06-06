def solution(n):
    arr = [i for i in range(1, n+1)]
    res = 0
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > n and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == n:
            res += 1
    
    return res