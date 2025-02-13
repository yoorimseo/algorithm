from collections import Counter

def solution(k, tangerine):
    types = Counter(tangerine).most_common()
    answer = 0
    
    for idx, (_, count) in enumerate(types, start=1):
        answer += count
        if answer >= k:
            return idx

    return len(types)