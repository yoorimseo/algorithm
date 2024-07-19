def solution(priorities, location):
    answer = 0
    origin = []
    for i in range(len(priorities)):
        origin.append((chr(65+i), priorities[i]))
    find = origin[location][0]

    sort_origin = []

    while origin:
        cmp = origin.pop(0)
        state = False

        for i in origin:
            if i[1] > cmp[1]:
                state = True
                break

        if state:
            origin.append(cmp)
        else:
            sort_origin.append(cmp)

    for i in range(len(sort_origin)):
        if sort_origin[i][0] == find:
            return i+1