word = input()
res = ''

for i in word:
    temp = (ord(i) - ord('A') - 3) % 26 + ord('A')
    res += chr(temp)

print(res)