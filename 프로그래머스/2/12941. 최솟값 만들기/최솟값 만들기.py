def solution(A,B):
    answer = 0

    if sum(A) < sum(B):
        A.sort()
        B.sort(reverse=True)
    else:
        A.sort(reverse=True)
        B.sort()

    for i in range(len(A)):
        answer += (A[i] * B[i])
    
    return answer