import sys
input = sys.stdin.readline

k = int(input())
signs = list(input().split())
visited = [False] * 10
res = []

def check(i, j, sign):
    if sign == '>':
        if i < j:
            return False
    else:
        if i > j:
            return False
    return True

def dfs(idx, temp):
    if idx == k+1:
        res.append(temp)
        return

    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(temp[idx-1], str(i), signs[idx-1]):
                visited[i] = True
                dfs(idx+1, temp+str(i))
                visited[i] = False

dfs(0, '')
print(max(res), min(res), sep='\n')