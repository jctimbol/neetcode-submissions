class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_len = len(nums)
        expected = (arr_len * (arr_len+1))//2

        for num in nums:
            expected -= num

        return expected