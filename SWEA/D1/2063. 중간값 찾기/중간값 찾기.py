N = int(input());

arr = list(map(int, input().split()));
arr.sort();

mid = len(arr) // 2;

print(arr[mid]);