class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)] # track (i, j) states

        res = [0, 0] # indices of start, end chars

        for i in range(n):
            # mark all 1 char substrings as palindromes
            dp[i][i] = True
        
        for i in range(n-1):
            # mark 2 char substrings as palindromes
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = [i, i+1]

        # mark the rest
        for width in range(2, n):
            for start in range(n - width):
                end = start + width
                # if width-2 window is palindrome, and s[start]
                # == s[end], then also palindrome

                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = True
                    res = [start, end]
        
        return s[res[0]:res[1]+1]

