class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        min k = 1           -> max h: sum(piles)
        max k = max(piles)  -> min h: len(piles)

        if k is too large


        1 2 3 4 5 6 7 8 9 10 ... 25
        if k = 12 -> h = 6 -> not enough; try higher
        k = 18 -> h = 6
        k = 21
        '''
        l = 1
        r = max(piles)
        mid = (l+r)//2
        res = r
        while l <= r:
            k = mid
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = mid
                r = mid-1
                mid = (l+r)//2

            else:
                l = mid+1
                mid = (l+r)//2
        return  res