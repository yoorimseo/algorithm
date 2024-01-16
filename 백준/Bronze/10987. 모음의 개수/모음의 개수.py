str = input()
cnt = 0

for i in str:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1

print(cnt)