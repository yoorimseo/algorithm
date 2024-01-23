def solution(spell, dic):
    answer = 0

    for i in dic:
        cnt = 0
        for j in spell:
            if j in i:
                cnt += 1

        if cnt == len(spell):
            answer += 1

    if answer == 0:
        return 2
    else:
        return 1