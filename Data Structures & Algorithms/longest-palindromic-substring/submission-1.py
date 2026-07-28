class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        
        longest = s[0]
        curr = ""
        for i in range(len(s)):
            curr += s[i]
            for j in range(i+1, len(s)):
                curr += s[j]
                if curr == curr[::-1] and len(curr) > len(longest):
                    longest = curr
            curr = ""

        return longest