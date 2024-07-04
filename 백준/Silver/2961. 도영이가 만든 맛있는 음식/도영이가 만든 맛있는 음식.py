N = int(input())
arr = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    arr.append([sour, bitter])
tmp = []
res = []

def combi(idx, tmp):
    if idx == N:
        if tmp:
            mul_ = 1
            add_ = 0
            for a in tmp:
                mul_ *= a[0]
                add_ += a[1]
            res.append(abs(mul_ - add_))
        return
    
    tmp.append(arr[idx])
    combi(idx+1, tmp)
    tmp.pop()
    combi(idx+1, tmp)

combi(0, [])
print(min(res))