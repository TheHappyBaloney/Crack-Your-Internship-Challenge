# 628. Maximum Product of Three Numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pro = nums[0] * nums[1] * nums[-1]
        orp = nums[-3] * nums[-2] * nums[-1]
   
        return max(pro,orp)
