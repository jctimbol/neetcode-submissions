class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        perm = s1
        while r < len(s2):
            if s2[r] in perm:
                for i in range(r, r+len(s1)):
                    if i < len(s2) and s2[i] in perm:
                        perm = perm.replace(s2[i], "", 1)
                    else:
                        break
                
                if not perm:
                    return True
                else:
                    perm = s1
            r += 1
        

        if not perm:
            return True
        return False