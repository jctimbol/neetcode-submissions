class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(path, remaining, index):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(index, len(nums)):
                if nums[i] > remaining:
                    break
                else:
                    path.append(nums[i])
                    backtrack(path, remaining - nums[i], i)
                    path.pop()
        

        backtrack([], target, 0)
        return res