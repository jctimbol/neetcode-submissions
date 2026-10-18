class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        remainder = n % 4
        expected = 0

        if remainder == 0:
            expected = n
        elif remainder == 1:
            expected = 1
        elif remainder == 2:
            expected = n+1
        else:
            expected = 0
        
        actual = nums[0]
        for num in nums[1:]:
            actual ^= num
        return expected ^ actual