T = int(input());

for i in range(1, T + 1):
    s = str(input());
    year = s[0:4];
    month = s[4:6];
    day = s[6:];

    days = {
        1: 31, 2: 28,
        3: 31, 4: 30,
        5: 31, 6: 30,
        7: 31, 8: 31,
        9: 30, 10: 31,
        11: 30, 12: 31
    };

    if 0 < int(month) < 12 and int(day) <= days[int(month)]:
        print(f"#{i} {year}/{month}/{day}");
    else:
        print(f"#{i} -1");