T = int(input());

for i in range(1, T + 1):
    arr = list(map(int, input().split(" ")));
    res = round(sum(arr) / 10)
    print(f"#{i} {res}");