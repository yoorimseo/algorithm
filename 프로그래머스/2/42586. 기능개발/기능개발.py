import math

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        tmp = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(tmp)

    for j in range(len(days)):
        if len(days):
            cmp = days.pop(0)
            cnt = 1

            for k in range(len(days)):
                if days[k] <= cmp:
                    cnt += 1
                else:
                    break

            if cnt != 1:
                days = days[cnt-1:]

            answer.append(cnt)
    return answer