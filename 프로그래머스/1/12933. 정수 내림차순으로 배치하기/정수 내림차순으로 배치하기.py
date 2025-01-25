def solution(n):
    answer = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(list(map(str, answer))))
    