class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for o in operations:
            if "++" in o:
                res += 1
            elif "--" in o:
                res -= 1
        return res
    