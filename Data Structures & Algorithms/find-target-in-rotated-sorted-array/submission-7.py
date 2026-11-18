class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            # pivot is not in left half
            if nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # pivot is not in right half
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        
        return -1
