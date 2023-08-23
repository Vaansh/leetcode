from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums) // 2
        counter = Counter(nums)
        for c, v in counter.items():
            if v > count:
                return c