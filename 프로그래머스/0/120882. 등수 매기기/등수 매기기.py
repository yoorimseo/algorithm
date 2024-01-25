def solution(score):
    avg = [sum(i) for i in score]
    sorted_avg = sorted(avg, reverse=True)
    rank = [sorted_avg.index(i) + 1 for i in avg]
    
    return rank