def solution(name, yearning, photo):
    answer = [0] * len(photo)
    point = dict()
    for i in range(len(name)):
        point[name[i]] = yearning[i]

    for j in range(len(photo)):
        for k in range(len(photo[j])):
            if photo[j][k] in point:
                answer[j] += point[photo[j][k]]

    return answer