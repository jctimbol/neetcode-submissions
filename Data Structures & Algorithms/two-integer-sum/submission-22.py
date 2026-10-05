class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value -> index
        vals = {}

        for i in range(len(nums)):
            vals[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in vals and i != vals[comp]:
                return [i, vals[comp]]

        return []