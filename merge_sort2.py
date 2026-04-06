nums = [1,9,2,8,5,3,4,7,6,0]
def merge(list,left,mid,right):
    extra = []
    beginning = left
    j = mid+1
    while left<=mid and j<=right:
        if list[left]>list[j]:
            extra.append(list[j])
            j+=1
        else:
            extra.append(list[left])
            left+=1
    while left<=mid:
        extra.append(list[left])
        left+=1
    while j<=right:
        extra.append(list[j])
        j+=1
    for i in range(len(extra)):
        list[beginning+i] = extra[i]
        
    


def separate(list,i,j):
    if i>=j:
        return
    mid = (i+j)//2
    separate(list,i,mid)
    
    separate(list,mid+1,j)
    merge(list,i,mid,j)

separate(nums,0,len(nums)-1) 
print(nums)