class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, path, index):
            res.append(path[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, path, i+1)
                path.pop()
            return
        backtrack(nums, [], 0)
        return res