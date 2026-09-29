class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        #case 1: rob first, exclude last
        dp_1 = [0 * i for i in range(len(nums)-1)]
        dp_1[0], dp_1[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            dp_1[i] = max(nums[i]+dp_1[i-2], dp_1[i-1])

        #case 2: rob last, exclude first
        dp_2 = [0 * i for i in range(len(nums)-1)]
        dp_2[0], dp_2[1] = nums[1], max(nums[1], nums[2])

        for i in range(3, len(nums)):
            dp_2[i-1] = max(nums[i]+dp_2[i-3], dp_2[i-2])
        
        print(dp_1, dp_2)
        return max(dp_1[-1], dp_2[-1])


        