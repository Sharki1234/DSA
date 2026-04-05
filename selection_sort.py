nums = [1,4,3,5,2,6]
n = len(nums)-1
for i in range(n):
    min_index = i
    for j in range(i+1,n+1):
        if nums[min_index]>nums[j]:
            min_index = j
    other = nums[i]
    nums[i] = nums[min_index]
    nums[min_index] = other
    
print(nums)