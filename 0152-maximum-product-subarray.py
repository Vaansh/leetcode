class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curr_max, curr_min = nums[0], 1, 1
        for n in nums:
            vals = (n, n * curr_max, n * curr_min)
            curr_max, curr_min = max(vals), min(vals)
            res = max(res, curr_max)
        return res


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         memo = {}
#         def helper(i, product):
#             if i == n:
#                 return product
#             if (i, product) in memo:
#                 return memo[(i, product)]
#             memo[(i, product)] = max(
#                 product if i != 0 else nums[0],
#                 max(helper(i + 1, nums[i]), helper(i + 1, product * nums[i])),
#             )
#             return memo[(i, product)]
#         return helper(0, 1)
