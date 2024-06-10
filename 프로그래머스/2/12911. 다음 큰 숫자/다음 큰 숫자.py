def solution(n):
    cnt_n = len(list(filter(lambda x: x == '1', format(n, 'b'))))
    answer = 0

    for i in range(n+1, 1000000):
        bin_i = format(i, 'b')
        cnt_i = len(list(filter(lambda x: x == '1', bin_i)))

        if cnt_i == cnt_n:
            return int(bin_i, 2)