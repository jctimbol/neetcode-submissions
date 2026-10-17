class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0

        for i in range(len(strs[0])):
            curr = strs[0][i]
            for string in strs:
                if i >= len(string) or string[i] != curr:
                    return res
            res += curr
        
        return res

                