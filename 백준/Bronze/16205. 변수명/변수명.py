N, name = input().split()
result = []

if N == '1' or N == '3':
    word = ""
    for char in name:
        if char.isupper():
            if word:
                result.append(word)
                word = ""
            word += char
        else:
            word += char
    if word:
        result.append(word)
elif N == '2':
    result = name.split('_')

def camelCase(arr):
    word = arr[0].lower()
    for i in arr[1:]:
        word += i[0].upper() + i[1:]

    return word

def snakeCase(arr):
    word = []
    for i in result:
        word.append(i.lower())
    return '_'.join(word)

def pascalCase(arr):
    word = ''
    for i in arr:
        word += i[0].upper() + i[1:]

    return word

camelCase = camelCase(result)
snakeCase = snakeCase(result)
pascalCase = pascalCase(result)

print(camelCase, snakeCase, pascalCase, sep='\n')