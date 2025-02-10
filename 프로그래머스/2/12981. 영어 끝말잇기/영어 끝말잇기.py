def solution(n, words):
    num, cnt = 0, 0
    cmp = words[0]

    for i in range(1, len(words)):
        if  words[:i+1].count(words[i]) > 1 or cmp[-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        cmp = words[i]

    return [0, 0]