class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # recursion -> check if each substring is subsequence
        # top down -> use a memo to cache each i, j state
        # states: 
        #  -1 (not visited)
        #   0 (not subsequence)
        #   1 (is subsequence)
        n, m = len(s), len(t)
        memo = [[-1] * m for i in range(n)]

        def recurse(i, j):
            print(i, j)
            # base case: reach end of s -> all matched
            if i == n:
                return True
            
            # base case: reach end of t but not s -> not all matched
            if j == m:
                return False
            
            if memo[i][j] != -1: # not visited
                return memo[i][j] == 1
            if s[i] == t[j]:
                memo[i][j] = 1 if recurse(i + 1, j + 1) else 0
            else:
                memo[i][j] = 1 if recurse(i, j + 1) else 0
            return memo[i][j] == 1
        
        return recurse(0, 0)