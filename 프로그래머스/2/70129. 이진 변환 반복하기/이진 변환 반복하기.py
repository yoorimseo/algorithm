def solution(s):
    zero, cnt = 0, 0
    
    while s != '1':
        zero += s.count('0')
        s = ''.join(list(filter(lambda x: x == '1', s)))
        length = len(s)
        s = str(format(int(length), 'b'))
        cnt += 1

    return [cnt, zero]