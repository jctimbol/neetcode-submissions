class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = []

        def backtrack(candidates, target, current, perms):
            if len(current) >= target:
                perms.append(current[:])
                return
            for cand in candidates:
                if cand not in current:
                    current.append(cand)
                    backtrack(candidates, target, current, perms)
                    current.remove(cand)
            return

        

        backtrack(nums, len(nums), [], perms)

        return perms
        