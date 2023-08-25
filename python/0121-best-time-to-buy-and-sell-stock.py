from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, inf

        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)

        return max_profit
