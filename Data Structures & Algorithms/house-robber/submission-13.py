class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            if i == 0 or i == 1:
                res.append(nums[i])
            elif i == 2:
                res.append(max(nums[i], nums[i]+res[i-2]))
            else:
                print(i, i-2)
                res.append(max(nums[i]+res[i-3], nums[i]+res[i-2]))

        print(res)
        return max(res)