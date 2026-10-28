class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_max = max(curr_max+num, num)
            max_sum = max(max_sum, curr_max)
        
        return max_sum