class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        pmax = 0
        while(r < len(prices)):
            if(prices[r] >= prices[l]):
                pmax = max(prices[r]-prices[l], pmax)
                r+=1
            else:
                l+=1
                r+=1
        
        r-=1
        print(r)
        while(l < r):
            if(prices[r] >= prices[l]):
                pmax = max(prices[r]-prices[l], pmax)
            l+=1

        return pmax