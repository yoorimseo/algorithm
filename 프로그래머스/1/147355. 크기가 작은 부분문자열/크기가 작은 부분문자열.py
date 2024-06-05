def solution(t, p):
    length = len(p)
    arr = []

    for i in range(len(t)):
        temp = t[i:length+i]

        if len(temp) == length:
            arr.append(''.join(temp))

    res = list(filter(lambda n: n <= p, arr))

    return len(res)