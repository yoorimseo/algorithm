while True:
    try:
        string = list(input())
        res = [0] * 4

        for i in string:
            if 97 <= ord(i) <= 122:
                res[0] += 1
            elif 65 <= ord(i) <= 90:
                res[1] += 1
            elif i == ' ':
                res[3] += 1
            else:
                res[2] += 1
        print(*res)
    except EOFError:
        break