class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        prev = None
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if not prev or time > prev:
                prev = time
                res += 1
        return res
