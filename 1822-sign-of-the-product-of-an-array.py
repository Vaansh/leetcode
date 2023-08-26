class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if n == 0:
                return 0
            res *= n
        return abs(res) // res
