T = int(input())

for i in range(T):
    string = input()
    if string == string[::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i + 1} 0')