class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0
        for n in nums:
            prev_max, curr_max = curr_max, max(prev_max + n, curr_max)
        return curr_max


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 3:
#             return max(nums)
#         @cache
#         def helper(i):
#             if i >= n:
#                 return 0
#             return max(nums[i] + helper(i + 2), helper(i + 1))
#         return helper(0)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 3:
#             return max(nums)
#         memo = {}
#         def helper(i):
#             if i >= n:
#                 return 0
#             if i in memo:
#                 return memo[i]
#             memo[i] =  max(nums[i] + helper(i + 2), helper(i + 1))
#             return memo[i]
#         return helper(0)
