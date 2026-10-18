class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy choice: if prices[r] is greater, then sell
        # optimal solution is made of locally optimal solutions

        profit = 0
        l, r = 0, 1
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit