num = list(map(int, input().split()))
num.remove(max(num))
print(max(num))