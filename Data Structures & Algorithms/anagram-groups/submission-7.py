class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)

        for i in range(len(strs)):
            seen[str(sorted(strs[i]))].append(strs[i])
        
        return list(seen.values())


        