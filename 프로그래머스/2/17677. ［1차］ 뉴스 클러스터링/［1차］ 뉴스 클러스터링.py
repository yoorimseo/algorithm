import math
from collections import Counter

def make_bigrams(s):
    bigrams = []
    s = s.upper()
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            bigrams.append(s[i] + s[i+1])
    return bigrams

def solution(str1, str2):
    bigrams1 = make_bigrams(str1)
    bigrams2 = make_bigrams(str2)

    counter1 = Counter(bigrams1)
    counter2 = Counter(bigrams2)

    intersection = counter1 & counter2
    union = counter1 | counter2

    intersection_count = sum(intersection.values())
    union_count = sum(union.values())

    if union_count == 0:
        answer = 65536
    else:
        answer = math.floor(intersection_count / union_count * 65536)
    return answer