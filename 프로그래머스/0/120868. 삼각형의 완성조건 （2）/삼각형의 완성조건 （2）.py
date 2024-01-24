def solution(sides):
    answer = []
    i = max(sides)
    while max(sides) < min(sides) + i:
        answer.append(i)
        i -= 1

    long = max(sides) + 1
    while long < sum(sides):
        answer.append(long)
        long += 1
    return len(answer)