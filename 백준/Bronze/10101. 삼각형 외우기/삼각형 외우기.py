x = int(input())
y = int(input())
z = int(input())

sum_tri = x + y + z

if x == y == z == 60:
    print('Equilateral')
elif sum_tri == 180:
    if (x == y or y == z or x == z):
        print('Isosceles')
    elif x != y != z:
        print('Scalene')
else:
    print('Error')