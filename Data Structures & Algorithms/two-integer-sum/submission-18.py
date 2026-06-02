class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        i = 0
        for num in nums:
            diff = target - num

            for j in range(0, len(nums)):
                if j == i:
                    continue
                if nums[j] == diff:
                    indices.append(i)
                    indices.append(j)
                    return indices
            i += 1
        return indices
