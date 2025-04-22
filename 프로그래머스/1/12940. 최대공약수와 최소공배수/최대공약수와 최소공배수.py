def solution(a, b):
    x, y = a, b
    
    while y != 0:
        x, y = y, x % y
    
    gcd = x
    lcm = (a * b) // gcd
    
    return [gcd, lcm]