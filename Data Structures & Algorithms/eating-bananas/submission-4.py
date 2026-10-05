class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        curr_k = 0
        min_k = r
        
        while l <= r:
            curr_k = (r + l) // 2
            curr_time = 0
            for pile in piles:
                curr_time += math.ceil(pile/curr_k)
            if curr_time > h:
                l = curr_k + 1
            else:
                min_k = min(min_k, curr_k)
                r = curr_k - 1
        
        return min_k