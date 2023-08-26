class Solution:
    def climbStairs(self, n: int) -> int:
        # n: 1 res: 1
        # n: 2 res: 1+1, 2=2
        # n: 3 res: 1+1+1, 1+2, 2+1=3
        # n: 4 res: 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2=5
        # n: 5 res: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2=8

        memo = {1: 1, 2: 2}

        def helper(num):
            if num in memo:
                return memo[num]
            memo[num] = helper(num - 1) + helper(num - 2)
            return memo[num]

        return helper(n)


# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         return self.climbStairs(n - 2) + self.climbStairs(n - 1)
