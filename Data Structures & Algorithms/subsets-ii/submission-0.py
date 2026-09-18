class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, path, index):
            print(nums)
            if path not in res:
                res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, path, i+1)
                path.pop()
            return
        backtrack(nums, [], 0)
        return res