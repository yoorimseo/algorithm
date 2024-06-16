def solution(food):
    cnt = []
    answer = ''

    for i in range(1, len(food)):
        if food[i] % 2 >= 0:
            cnt.append(food[i] // 2)

    for j in range(len(cnt)):
        answer += (str(j+1) * cnt[j])

    return answer + '0' + answer[::-1]