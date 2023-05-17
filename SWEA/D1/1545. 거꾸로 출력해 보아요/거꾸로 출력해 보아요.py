N = int(input());
arr = list(range(0, N + 1));
arr.sort(reverse=True);

print(*arr);