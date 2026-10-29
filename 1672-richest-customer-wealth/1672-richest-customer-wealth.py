class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_sum=float(-inf)
        for row in accounts:
            max_sum=max(max_sum,sum(row))
        return max_sum


        