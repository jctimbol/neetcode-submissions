class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid] <= nums[r]: #normal
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            else:
                #partition in left half
                if nums[l] > nums[mid]:
                    if nums[mid] <= target <= nums[r]: #target in right sorted half
                        l = mid+1
                    else:
                        r = mid-1

                #partition in right half
                elif nums[r] < nums[mid]:
                    if nums[l] <= target <= nums[mid]:
                        r = mid-1
                    else:
                        l = mid+1
        return -1