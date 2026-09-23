class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(idx, path):
            #base case: idx @ end
            if idx == len(s):
                res.append(path[:])
                return
            #look @ substrings starting at idx
            for i in range(idx+1, len(s)+1):
                substring = s[idx:i]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(i, path)
                    path.pop()
        
        backtrack(0, [])
        print(res)
        return res