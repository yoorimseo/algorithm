def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        
        for j in range(len(arr1[i])):
            num = arr1[i][j] + arr2[i][j]
            temp.append(num)
            
        answer.append(temp)
    
    return answer