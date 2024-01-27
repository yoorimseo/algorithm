import math

def solution(numer1, denom1, numer2, denom2):
    answer = [0]*2
    x1, y1 = numer1 * denom2, denom1 * denom2
    x2, y2 = numer2 * denom1, denom2 * denom1
    n, m = x1 + x2, y1
    
    gcd = math.gcd(n, m)
    answer[0] = n // gcd
    answer[1] = m // gcd
    
    return answer