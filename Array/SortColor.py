# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, n = 0 , 0 , len(nums)
        for i in range (n):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1

        for i in range(0, zero):
            nums[i] = 0
        
        for i in range(zero, zero + one):
            nums[i] = 1

        for i in range(zero + one , n):
            nums[i] = 2
        
