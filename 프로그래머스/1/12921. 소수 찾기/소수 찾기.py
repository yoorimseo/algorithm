def solution(n):
    answer = 0
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False

    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False

    for i in range(n+1):
        if prime[i]:
            answer += 1
            
    return answer