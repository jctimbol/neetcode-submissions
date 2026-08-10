class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]
        for num in nums:
            tmp = curMax * num # might now be min
            curMax = max(num, tmp, num*curMin)
            curMin = min(num, num*curMin, tmp)
            res = max(res, curMax)
        print(curMin, curMax)
        return res