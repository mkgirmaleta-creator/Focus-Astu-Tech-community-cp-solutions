nums = [1,3,5,6], target = 5
index=0
for i in len(nums):
    if nums[i]==target:
        index=i
    elif target<=nums[i]:
        index=i
    else:
        index=len(nums)-1
