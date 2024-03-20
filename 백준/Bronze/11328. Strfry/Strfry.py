N = int(input())

for _ in range(N):
    A, B = input().split()
    A = ''.join(sorted(A))
    B = ''.join(sorted(B))

    for i in range(len(A)):
        if A[i] != B[i]:
            flag = False
            break
        else:
            flag = True

    if flag:
        print("Possible")
    else:
        print("Impossible")