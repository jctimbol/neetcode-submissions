class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while (r-l+1) > k:
            d1 = abs(arr[l]-x)
            d2 = abs(arr[r]-x)
            if d1 < d2: # arr[l] is closer
                r -= 1
            elif d1 > d2:
                l += 1
            elif l < r:
                r -= 1
            else:
                l += 1
        
        return arr[l:r+1]
        
