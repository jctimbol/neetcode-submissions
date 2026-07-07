class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1           # min k
        r = max(piles)  # max k
        mid = (l+r) // 2
        min_k = r

        while l <= r:
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                r = mid - 1
                min_k = min(min_k, mid)
            else:
                l = mid + 1

            mid = (l + r) // 2

        return min_k
        