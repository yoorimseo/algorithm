length = int(input())
arr = list(input())

two = list(filter(lambda s: s == '2', arr))
e = list(filter(lambda s: s == 'e', arr))

if len(two) > len(e):
    print('2')
elif len(two) < len(e):
    print('e')
else:
    print('yee')