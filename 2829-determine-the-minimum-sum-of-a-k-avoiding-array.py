class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res, curr, size, seen = 0, 1, 0, set()
        while size < n:
            if curr not in seen:
                res += curr
                size += 1
                seen.add(k - curr)
            curr += 1
        return res
