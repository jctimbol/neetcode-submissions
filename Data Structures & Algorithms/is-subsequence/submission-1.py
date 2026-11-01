class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # recursion -> check if each substring is subsequence

        def recurse(i, j):
            # base case: reach end of s -> all matched
            if i == len(s):
                return True
            
            # base case: reach end of t but not s -> not all matched
            if j == len(t):
                return False
            
            if s[i] == t[j]:
                return recurse(i + 1, j + 1)
            
            return recurse(i, j + 1)
        
        return recurse(0, 0)
            