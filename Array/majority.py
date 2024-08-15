# 169. Majority Element

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        res , freq =  count.most_common(1)[0]

        return res
