class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(numbers):
            complement = target - n
            if complement in d:
                return [d[complement] + 1, i + 1]
            d[n] = i