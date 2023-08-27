class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res = 1
        pairs.sort(key=lambda x: x[1])
        prev = pairs[0]
        for p in pairs:
            if p[0] > prev[1]:
                res += 1
                prev = p
        return res
