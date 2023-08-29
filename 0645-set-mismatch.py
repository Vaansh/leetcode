class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a, b = sum(nums), sum(set(nums))
        return [a - b, sum(range(1, len(nums) + 1)) - b]
