def convert_to_base(n, base):
    digits = "0123456789ABCDEF"

    if n == 0:
        return "0"

    result = ""

    while n > 0:
        result = digits[n % base] + result
        n //= base

    return result


def solution(n, t, m, p):
    sequence = ""
    number = 0

    while len(sequence) < t * m:
        sequence += convert_to_base(number, n)
        number += 1

    result = ""
    
    for i in range(p - 1, t * m, m):
        result += sequence[i]

    return result