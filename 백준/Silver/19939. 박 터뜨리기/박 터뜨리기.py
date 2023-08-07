N, K = map(int, input().split())
min_K = K * (K + 1) // 2

if N < min_K:
    print(-1)
elif (N - min_K) % K == 0:
    print(K - 1)
else:
    print(K)