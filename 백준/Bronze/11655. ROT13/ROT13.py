string = input()
res = ''

for i in string:
    temp = ord(i)+13
    if 65 <= ord(i) <= 90:
        res += chr(temp - 26 if temp > 90 else temp)
    elif 97 <= ord(i) <= 122:
        res += chr(temp - 26 if temp > 122 else temp)
    else: res += i

print(res)