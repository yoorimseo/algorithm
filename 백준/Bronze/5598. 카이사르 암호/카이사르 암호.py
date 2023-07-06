from string import ascii_uppercase

alphabet = list(ascii_uppercase)
str = input()
arr = list(str)
res = ''

for s in arr:
    index = alphabet.index(s) - 3
    res += alphabet[index]

print(res)