def solution(n):
    binary = format(n, 'b')
    ans = list(filter(lambda s: s == '1', binary))

    return len(ans)