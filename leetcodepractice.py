height = [1,2]
#first get the largest value
max = 0
index = 0
for i in range(len(height)):
    if height[i]>max:
        max = height[i]
        index = i


for j in range(len(height)):
    value = ((j-(index))*height[j])
    
    if value>max and j!=index:
        max = value
print(max)
