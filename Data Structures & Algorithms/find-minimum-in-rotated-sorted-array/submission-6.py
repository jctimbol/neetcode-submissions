class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')

        l, r = 0, len(nums)-1
        mid = 0
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            else:
                mid = (l+r)//2
                if nums[l] < nums[mid]:
                    l = mid
                else:
                    r = mid
        
        return nums[mid+1] if mid+1<len(nums) else nums[0]
