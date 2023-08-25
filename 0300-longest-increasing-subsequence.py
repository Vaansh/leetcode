class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        return max(res)


# from math import inf
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = [inf]
#         for n in reversed(nums):
#             for i in range(len(memo) - 1, -1, -1):
#                 if n > memo[i]:
#                     continue
#                 elif n == memo[i]:
#                     break
#                 elif i == len(memo) - 1:
#                     memo.append(n)
#                 else:
#                     memo[i + 1] = n
#                 break
#         return len(memo) - 1
