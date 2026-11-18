class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            # pivot sits in (mid, r]
            if nums[mid] > nums[r]:
                l = mid+1
            # pivot sits in [l, mid]
            else:
                r = mid
        
        return nums[l]