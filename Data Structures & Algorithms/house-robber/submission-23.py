class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo
        memo = {i: -1 for i in range(len(nums))}

        def rec(i):
            length = len(nums[i:])
            if length == 0:
                return 0
            
            # visited
            if memo[i] != -1:
                return memo[i]
            
            # not visited
            memo[i] = max(rec(i+1), rec(i+2) + nums[i])

            return memo[i]
        
        return rec(0)