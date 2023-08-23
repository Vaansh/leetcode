class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        max_num = -1

        if len(arr) == 0:
            return res
        
        res.append(-1)
        for i in range(len(arr) - 1, 0, -1):
            max_num = max(max_num, arr[i])
            res.append(max_num)

        return res[::-1]