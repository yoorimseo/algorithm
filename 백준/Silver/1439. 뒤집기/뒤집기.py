str = input()
zero = 0
one = 0

if str[0] == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(str)):
    if str[i - 1] != str[i]:
        if str[i] == '1':
            one += 1
        else:
            zero += 1

print(min(zero, one))