def solution(s):
    arr = []
    for i in s.split("},"):
        tmp = list(map(int, i.replace("{","").replace("}","").split(",")))
        arr.append(tmp)

    arr.sort(key=len)
    
    answer = []

    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return answer