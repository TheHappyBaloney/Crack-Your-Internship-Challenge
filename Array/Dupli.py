# 442. Find All Duplicates in an Array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupli = []
        seen = set()
        n = len(nums)
        for i in nums:
            if i in seen:
                dupli.append(i)
            else:
                seen.add(i)

        return dupli
