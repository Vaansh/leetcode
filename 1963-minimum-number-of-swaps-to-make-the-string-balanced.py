class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0

        for c in s:
            if c == "[":
                res += 1
            elif res != 0:
                res -= 1

        return (res + 1) // 2