class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            c = target - n
            if c in d:
                return [d[c] + 1, i + 1]
            d[n] = i
