class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        min_value=prices[0]
        for price in prices:
            min_value=min(min_value,price)
            max_profit=max(max_profit,price-min_value)
        return max_profit
        