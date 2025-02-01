def solution(s):
    zero = 0
    cnt = 0

    while s != '1':
        zero += s.count('0')

        c = s.replace('0', '')
        s = str(format(len(c), 'b'))

        cnt += 1
    
    return [cnt, zero]