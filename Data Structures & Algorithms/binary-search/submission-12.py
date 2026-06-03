class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        m = len(nums) // 2
        r = len(nums) - 1
        for i in range(0, len(nums)//2 + 1):
            if(nums[m] == target):
                 return m
            elif(nums[m] > target):
                r = m - 1
                m = (l + r) // 2
            else:
                l = m + 1
                m = (l + r) // 2
        return -1
