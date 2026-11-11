class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numbers = set(nums)
        for num in nums:
            curr = num
            seq = 1
            if num-1 not in numbers:
                while curr in numbers:
                    seq += 1
                    curr += 1
            res = max(res, seq-1)
        return res