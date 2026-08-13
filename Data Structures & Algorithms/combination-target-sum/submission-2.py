class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currentPath = []
        nums.sort()
        def backtrack(index, target, currentPath, res):
            if target == 0:
                res.append(list(currentPath))
                return
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break
                currentPath.append(nums[i])
                backtrack(i, target-nums[i], currentPath, res)
                currentPath.pop()

        backtrack(0, target, currentPath, res)

        return res