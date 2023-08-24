class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(target):
            if target < 0:
                return 0

            if target == 0:
                return 1

            if target in memo:
                return memo[target]

            ways = 0
            for n in nums:
                ways += helper(target - n)
            memo[target] = ways
            return ways

        return helper(target)
