class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, r = 0, len(s1)-1
        counts = {}
        for char in s1:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        
        while r < len(s2):
            curr_counts = {}
            for i in range(l, r+1):
                char = s2[i]
                if char not in curr_counts:
                    curr_counts[char] = 1
                else:
                    curr_counts[char] += 1

            if counts == curr_counts:
                return True
            else:
                l += 1
                r += 1
        
        return False