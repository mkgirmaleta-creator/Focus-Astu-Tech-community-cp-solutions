nums =[3,2,3]
target =6
ans=[]
l,r=0,len(nums)-1
while l<r:
    if nums[l]+nums[r]!=target:
        l+=1
        r-=1
    if nums[l]+nums[r]==target:
        ans.extend([l,r])
print(ans)

