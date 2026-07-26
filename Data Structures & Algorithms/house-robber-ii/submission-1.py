class Solution:
    def rob(self, nums: List[int]) -> int:
        res1, res2 = [], []
        if len(nums) <= 3:
            return max(nums)

        for i in range(len(nums)-1):
            if i == 0 or i == 1:
                res1.append(nums[i])
            elif i == 2:
                res1.append(max(nums[i], nums[i]+res1[i-2]))
            else:
                res1.append(max(nums[i]+res1[i-3], nums[i]+res1[i-2]))


        for i in range(1, len(nums)):
            if i == 1 or i == 2:
                res2.append(nums[i])
            elif i == 3:
                res2.append(max(nums[i], nums[i]+res2[i-3]))
            else:
                res2.append(max(nums[i]+res2[i-4], nums[i]+res2[i-3]))
        print(res1, res2)
        return max(max(res1), max(res2))