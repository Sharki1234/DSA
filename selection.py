nums = [5,1,2,3,1]
n = len(nums)
#maxi = 
maxi_index = 0
for i in range(n):
    maxi = nums[i]
    maxi_index = i
    for j in range(n-i):
        if nums[j]<=maxi:
            maxi = nums[j]
            maxi_index = j
    nums[maxi_index] = nums[(n-i-1)]
    nums[(n-i-1)]=maxi
    #maxi = 0
    print(nums)
print(nums)