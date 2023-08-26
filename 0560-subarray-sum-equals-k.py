class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = s = 0
        d = {}

        for n in nums:
            s += n
            res += s == k
            c = s - k
            res += d.get(c, 0)
            d[s] = d.get(s, 0) + 1

        return res
