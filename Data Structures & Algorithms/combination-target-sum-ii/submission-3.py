class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(candidates, target, path, index):
            if target == 0:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if candidates[i] <= target:
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    path.append(candidates[i])   
                    backtrack(candidates, target-candidates[i], path, i+1)
                    path.pop()
            return
        backtrack(candidates, target, [], 0)
        return res
