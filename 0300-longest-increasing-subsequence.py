class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [inf]

        for n in reversed(nums):
            for i in range(len(memo) - 1, -1, -1):
                if n > memo[i]:
                    continue
                elif n == memo[i]:
                    break
                elif i == len(memo) - 1:
                    memo.append(n)
                else:
                    memo[i + 1] = n
                break

        return len(memo) - 1
