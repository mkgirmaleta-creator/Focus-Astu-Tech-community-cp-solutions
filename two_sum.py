class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ans.extend([i,j])
        return ans
