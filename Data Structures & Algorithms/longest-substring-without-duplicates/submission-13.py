class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        max_len = 0
        
        while r < len(s):
            curr_len = r-l+1
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                curr_len -= 1
            
            seen.add(s[r])
            max_len = max(max_len, curr_len)
            r += 1
        
        return max_len
            

            