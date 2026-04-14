class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        a=0
        l,r=0,l+1
        while r<len(nums):
            if nums[r]-nums[l]==1:
                m+=1
                r+=1
            else:r+=1
            if r==len(nums)-1:
                l+=1
                r=l+1
                a=max(m,a)
        return a


        
