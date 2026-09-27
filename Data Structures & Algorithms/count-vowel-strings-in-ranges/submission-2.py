class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counts = [0 * i for i in range(len(words))]
        vowels = "aeiou"
        res = []
        
        #prefix sum are
        i=0
        curr = 0
        for word in words:
            if word[0] in vowels and word[len(word)-1] in vowels:
                curr += 1
            counts[i] = curr
            i += 1

        print(counts)

        for li, ri in queries:
            if li > 0:
                res.append(counts[ri]-counts[li-1])
            else:
                res.append(counts[ri])
        return res