X = input()
cnt = 0

while len(X) > 1:
    cnt += 1
    Y = sum(list(map(int, X)))
    X = str(Y)

if int(X) % 3 == 0:
    print(cnt, 'YES', sep='\n')
else:
    print(cnt, 'NO', sep='\n')
    