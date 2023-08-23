class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        prev = None
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if not prev or t > prev:
                prev = t
                res += 1
        return res
