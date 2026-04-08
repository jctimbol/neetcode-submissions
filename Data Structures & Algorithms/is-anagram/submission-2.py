class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted1 = sorted(s)
        sorted2 = sorted(t)
        return sorted1 == sorted2