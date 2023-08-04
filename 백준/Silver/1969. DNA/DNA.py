n, m = list(map(int, input().strip().split()))
dna_list = [input().strip() for _ in range(n)]
res_cnt = 0
res_str = ''

for i in range(0, m):
    arr = [0, 0, 0, 0] # A C G T 순

    for j in range(0, n):
        if dna_list[j][i] == 'A':
            arr[0] += 1
        elif dna_list[j][i] == 'C':
            arr[1] += 1
        elif dna_list[j][i] == 'G':
            arr[2] += 1
        elif dna_list[j][i] == 'T':
            arr[3] += 1

    max_idx = arr.index(max(arr))

    if max_idx == 0:
        res_str += 'A'
    elif max_idx == 1:
        res_str += 'C'
    elif max_idx == 2:
        res_str += 'G'
    elif max_idx == 3:
        res_str += 'T'
        
    res_cnt += sum(arr) - max(arr)

print(res_str)
print(res_cnt)