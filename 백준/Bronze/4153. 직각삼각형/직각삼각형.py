while True:
    arr = list(map(int, input().split()))

    if sum(arr) == 0:
        break

    c = max(arr)
    arr.remove(c)

    if arr[0] ** 2 + arr[1] ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')