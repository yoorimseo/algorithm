def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])

    for i in range(m):
        tmp = arr1[i]
        result = []
        
        for j in range(r):
            num = 0
            
            for k in range(n):
                num += tmp[k] * arr2[k][j]
            result.append(num)
            
        answer.append(result)
        
    return answer