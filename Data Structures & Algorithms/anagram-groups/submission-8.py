class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimize the per-string sorting through a character count
        # hashable via tuples

        seen = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char)-ord('a')] += 1
            
            seen[tuple(count)].append(s)
        
        return list(seen.values())
