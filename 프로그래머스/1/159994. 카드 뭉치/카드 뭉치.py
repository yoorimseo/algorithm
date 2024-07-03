def solution(cards1, cards2, goal):
    answer = 'Yes'

    while goal:
        cmp = goal.pop(0)

        if len(cards1) and cards1[0] == cmp:
            cards1.pop(0)
        elif len(cards2) and cards2[0] == cmp:
            cards2.pop(0)
        else:
            answer = 'No'
            break

    return answer