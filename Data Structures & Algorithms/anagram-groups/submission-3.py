class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_map = {} # sorted string -> index
        res = []
        for i in range(len(strs)):
            curr = strs[i]
            sorted_curr = ''.join(sorted(curr))
            if sorted_curr in seen_map:
                idx = seen_map[sorted_curr]
                res[idx].append(curr)
                continue
            else: # new
                res.append([curr])
                seen_map[sorted_curr] = len(res) - 1
        return res
            