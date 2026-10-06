class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, candidates, path):
            res.append(path[:])

            for i in range(index, len(candidates)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i, nums, path)
                    path.pop()
        
        backtrack(0, nums, [])
        return res
