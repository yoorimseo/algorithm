import math

def solution(arr):
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    answer = arr[0]

    for i in arr[1:]:
        answer = lcm(answer, i)

    return answer