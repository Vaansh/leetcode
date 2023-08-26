class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        res = 0
        profits = {}

        for o in offers:
            profits.setdefault(o[0], []).append([o[1], o[2]])

        arr = [0] * n

        for o in range(n):
            if o in profits:
                for p in profits[o]:
                    arr[p[0]] = max(arr[p[0]], p[1] + res)
            res = max(res, arr[o])

        return res
