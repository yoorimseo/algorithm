N = int(input())

for _ in range(N):
    arr = list(input())
    new = []

    for i in range(len(arr)):
        if i == 0:
            new.append(arr[i])
        else:
            if len(new) == 0:
                new.append(arr[i])
            elif arr[i] == ')' and new[-1] == '(':
                new.pop()
            else:
                new.append(arr[i])

    if len(new) == 0:
        print('YES')
    else:
        print('NO')