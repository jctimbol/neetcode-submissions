class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = nums[0]

        for num in nums:
            tmp = curMax * num
            curMax = max(num, num*curMax, num*curMin)
            curMin = min(num, num*curMin, tmp)
            res = max(res, curMax)

        return res