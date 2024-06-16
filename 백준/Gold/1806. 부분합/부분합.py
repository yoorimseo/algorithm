N, S = map(int, input().split())
arr = list(map(int, input().split()))

def solve():
    low, high = 0, 0
    my_sum = arr[0]
    length = N + 1

    while True:
        if my_sum < S:
            high += 1
            if high == N:
                break

            my_sum += arr[high]
        else:
            length = min(length, high - low + 1)
            my_sum -= arr[low]
            low += 1

    return 0 if length == N + 1 else length

print(solve())