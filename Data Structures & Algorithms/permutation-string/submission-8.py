class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for char in s1:
            if char not in target:
                target[char] = 1
            else:
                target[char] += 1


        l, r = 0, len(s1) - 1
        while r < len(s2):
            curr = {}
            for i in range(l, r+1):
                if s2[i] not in curr:
                    curr[s2[i]] = 1
                else:
                    curr[s2[i]] += 1
            
            if curr == target:
                return True
            
            l += 1
            r += 1
        
        return False