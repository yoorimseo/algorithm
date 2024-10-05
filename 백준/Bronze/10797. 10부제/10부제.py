day = int(input())
car_day = list(map(int, input().split()))
res = list(filter(lambda x: x == day, car_day))

print(len(res))