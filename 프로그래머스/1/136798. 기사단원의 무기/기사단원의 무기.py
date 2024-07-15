def count_divisors(n):
    count = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
    return count

def solution(number, limit, power):
    answer = []

    for i in range(1, number + 1):
        cmp = count_divisors(i)
        if cmp > limit:
            cmp = power
        answer.append(cmp)
    
    return sum(answer)