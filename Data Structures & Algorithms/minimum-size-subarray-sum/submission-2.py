class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
            
        min_length = len(nums)

        l, r = 0, 1
        curr_sum = nums[0]

        while r < len(nums):
            if curr_sum >= target and l <= r:
                print(l, r)
                min_length = min(min_length, r-l)
                curr_sum -= nums[l]
                l += 1
                continue
            curr_sum += nums[r]
            r += 1

        r -= 1
        while l < len(nums):
            if curr_sum >= target:
                min_length = min(min_length, r-l+1)
            curr_sum -= nums[l]
            l += 1

        return min_length