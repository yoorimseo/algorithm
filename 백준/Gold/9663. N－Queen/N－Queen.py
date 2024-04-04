N = int(input())
arr = [0] * N

def is_possible(r):
    for i in range(r):
        if arr[r] == arr[i]:
            return False

        if r - i == abs(arr[r] - arr[i]):
            return False

    return True

def dfs(row):
    if row == N:
        return 1

    res = 0

    for i in range(N):
        arr[row] = i

        if is_possible(row):
            res += dfs(row + 1)

    return res

print(dfs(0))