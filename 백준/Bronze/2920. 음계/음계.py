nums = list(map(int, input().split()))

if sorted(nums) == nums:
    print('ascending')
elif sorted(nums, reverse=True) == nums:
    print('descending')
else:
    print('mixed')