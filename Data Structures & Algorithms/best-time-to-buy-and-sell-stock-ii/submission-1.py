class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        prev = -1
        while r < len(prices):
            if prev > prices[r]:
                max_profit += (prev-prices[l])
                l = r
                prev = -1
            elif prices[r] >= prices[l]:
                prev = prices[r]
            else:
                l = r
            r += 1
        max_profit += (prices[r-1]-prices[l])
        return max_profit