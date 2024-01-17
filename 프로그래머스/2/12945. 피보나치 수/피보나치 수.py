def solution(n):
    f0 = 0
    f1 = 1
    
    for _ in range(n):
        f0, f1 = f1, f0 + f1
    
    return f0 % 1234567