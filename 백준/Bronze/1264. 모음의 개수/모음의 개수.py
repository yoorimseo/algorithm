while True:
    s = input().lower()
    cnt = 0

    if s == '#':
        break

    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            cnt += 1

    print(cnt)
