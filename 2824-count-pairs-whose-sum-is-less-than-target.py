class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1
        return res


# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         res = set()
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] < target:
#                     res.add((i, j))
#         return len(res)
