class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # dp to store (i, j) states
        # -1 
        n, m = len(s), len(t)
        dp = [[-1] * m for i in range(n)]

        def rec(i, j):
            if i == n:
                return True
            if j == m:
                return False
            
            # visited
            if dp[i][j] != -1:
                return dp[i][j] == 1
            
            # not visited
            if s[i] == t[j]:
                dp[i][j] = 1 if rec(i+1, j+1) else 0
            else:
                dp[i][j] = 1 if rec(i, j+1) else 0
            
            return dp[i][j] == 1

        return rec(0, 0)
            
