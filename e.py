nums =[3,2,3]
target =6
ans=[]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            ans.extend([i,j])
print(ans)

