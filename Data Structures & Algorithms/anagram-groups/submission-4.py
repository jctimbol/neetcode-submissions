class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = defaultdict(list)

        for i in range(len(strs)):
            sorted_curr = ''.join(sorted(strs[i]))
            string_map[sorted_curr].append(strs[i])
        
        return list(string_map.values())