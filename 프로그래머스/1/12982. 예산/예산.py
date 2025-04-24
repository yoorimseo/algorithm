def solution(d, budget):
    d.sort()
    
    count = 0
    total = 0
    
    for cost in d:
        if total + cost <= budget:
            total += cost
            count += 1
        else:
            break
            
    return count