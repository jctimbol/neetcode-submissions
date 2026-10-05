class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
            else:
                max_profit = max(prices[r]-prices[l], max_profit)
                r += 1
                

        return max(0, max_profit)