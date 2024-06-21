def solution(k, score):
    answer = []
    rank = []

    for i in score:
        if len(rank) < k:
            rank.append(i)
        else:
            if i > rank[0]:
                rank.remove(rank[0])
                rank.append(i)

        rank.sort()
        answer.append(rank[0])
    return answer