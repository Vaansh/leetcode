class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b, c = nums.count(0), nums.count(1), nums.count(2)

        for i in range(a):
            nums[i] = 0

        for i in range(a, a + b):
            nums[i] = 1

        for i in range(a + b, a + b + c):
            nums[i] = 2
