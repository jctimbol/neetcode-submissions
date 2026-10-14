class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each element, is it better to add to subarray, or start a new one?
        # -> max(curr_sum + num, num)
        max_sum = -10001
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum