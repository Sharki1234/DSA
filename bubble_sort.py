nums = [1,7,3,5,4,7,6]
max = 0
n = len(nums)
for i in range(len(nums)-1):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            other = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = other
print(nums)
