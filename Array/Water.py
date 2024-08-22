# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = i = 0 
        j = len(height) - 1

        while i < j:
            if height[i] < height[j]:
                smallest = height[i]
            else:
                smallest = height[j]
            
            area = smallest * (j - i)

            m = area if area > m else m

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return m
             
