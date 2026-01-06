nums = [1,66,7,9,4,5,3]
n = len(nums)
for i in range(n):
    flag = False
    for j in range((n-i)-1):
        if nums[j] > nums[j+1]:
            flag = True
            other = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = other
    if not flag:
        break
print(nums)
#print(nums)

