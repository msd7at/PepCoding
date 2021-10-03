class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans=0
        g=nums[0]
        lmax=nums[0]
        for i in range(len(nums)):
            if g<nums[i]:
                g=nums[i]
            elif lmax > nums[i]:
                ans=i
                lmax=g
        return ans+1 
