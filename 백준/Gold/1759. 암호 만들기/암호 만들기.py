L, C = map(int, input().split())
S = sorted(list(input().split()))
word = []

def check(word):
    v_cnt, c_cnt = 0, 0

    for i in word:
        if i in ['a', 'e', 'i', 'o', 'u']:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt > 0 and c_cnt >= 2:
        return True
    else:
        return False

def dfs(start):
    if len(word) == L:
        if check(word):
            print(''.join(word))

    for i in range(start, C):
        word.append(S[i])
        dfs(i+1)
        word.pop()

dfs(0)