class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1,1

        for i in range(len(nums)):
            tmp = curr_max * nums[i]
            curr_max = max(nums[i], nums[i]*curr_max, nums[i]*curr_min)
            curr_min = min(tmp, nums[i], nums[i]*curr_min)

            res = max(res, curr_max)
            

        return res