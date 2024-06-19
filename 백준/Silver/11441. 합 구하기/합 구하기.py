N = int(input())
arr = list(map(int, input().split()))
sum_arr = [0] * (N+1)
for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

def acc(i, j):
    return sum_arr[j] - sum_arr[i - 1]

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(acc(i, j))