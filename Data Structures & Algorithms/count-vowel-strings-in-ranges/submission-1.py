class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counts = [0 * i for i in range(len(words))]
        vowels = "aeiou"
        res = []
        
        i=0
        for word in words:
            if word[0] in vowels and word[len(word)-1] in vowels:
                counts[i] += 1
            i += 1

        for li, ri in queries:
            res.append(sum(counts[li:ri+1]))
        return res