x_points = []
y_points = []

for _ in range(3):
    x, y = map(int, input().split())

    if x not in x_points:
        x_points.append(x)
    else:
        x_points.remove(x)

    if y not in y_points:
        y_points.append(y)
    else:
        y_points.remove(y)

print(*x_points, *y_points)