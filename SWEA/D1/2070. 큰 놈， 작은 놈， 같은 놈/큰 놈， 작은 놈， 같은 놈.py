T = int(input());

for i in range(1, T + 1):
    A, B = map(int, input().split(" "));
    if A == B:
        res = "=";
    elif A > B:
        res = ">";
    else:
        res = "<";
    print(f"#{i} {res}");