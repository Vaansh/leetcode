class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def helper(i, curr_sum):
            if curr_sum == target:
                return True

            if i >= len(nums) or curr_sum > target:
                return False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            if helper(i + 1, curr_sum + nums[i]):
                memo[(i, curr_sum)] = True
                return True

            if helper(i + 1, curr_sum):
                memo[(i, curr_sum)] = True
                return True

            memo[(i, curr_sum)] = False
            return False

        return helper(0, 0)
