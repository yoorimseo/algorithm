from collections import Counter

def solution(k, tangerine):
    answer = 0
    type = sorted(Counter(tangerine).items(), reverse=True, key=lambda x: x[1])

    for key, value in type:
        if k <= 0:
            break

        k -= value
        answer += 1

    return answer