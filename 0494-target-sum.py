class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)

        memo = {}

        def helper(i, curr_sum):
            if i == n:
                return curr_sum == target

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            memo[(i, curr_sum)] = helper(i + 1, curr_sum + nums[i]) + helper(
                i + 1, curr_sum - nums[i]
            )

            return memo[(i, curr_sum)]

        return helper(0, 0)
