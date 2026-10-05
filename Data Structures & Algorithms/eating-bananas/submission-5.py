class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            curr_k = (l+r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile/curr_k)
            
            if time > h:
                l = curr_k + 1
            else:
                res = min(curr_k, res)
                r = curr_k - 1
        
        return res