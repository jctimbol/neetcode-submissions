class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # shrink 2 ptrs
        l, r = 0, len(arr) - 1

        while (r-l+1) > k:
            print(l, r)
            l_distance = abs(arr[l]-x)
            r_distance = abs(arr[r]-x)

            if l_distance > r_distance:
                l += 1
            elif l_distance < r_distance:
                r -= 1
            elif l > r:
                l += 1
            else:
                r -= 1
        
        return arr[l:r+1]