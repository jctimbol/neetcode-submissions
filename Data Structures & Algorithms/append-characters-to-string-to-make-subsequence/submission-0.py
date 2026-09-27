class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i, j = 0, 0
        
        remaining = len(t)

        while i < len(s):
            print(s[i], s[j])
            if j >= len(t):
                break
            if s[i] == t[j]:
                j += 1
                remaining -= 1
            i += 1
            
        
        return remaining
