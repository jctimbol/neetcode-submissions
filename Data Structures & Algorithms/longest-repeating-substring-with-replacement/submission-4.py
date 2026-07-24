class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=0
        the_max = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r-l+1)-max(count.values()) > k: #invalid
                count[s[l]] -=1
                l += 1
                
            the_max = max(the_max, r-l+1)
        return the_max
        