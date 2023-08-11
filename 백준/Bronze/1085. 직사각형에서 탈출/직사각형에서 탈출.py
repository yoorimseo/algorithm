x, y, w, h = map(int, input().split())
line = [w - x, x - 0, h - y, y - 0]

print(min(line))