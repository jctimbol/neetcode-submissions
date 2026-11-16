class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path, remaining, index):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(path, remaining-candidates[i], i+1)
                path.pop()
            return
        
        backtrack([], target, 0)
        return res