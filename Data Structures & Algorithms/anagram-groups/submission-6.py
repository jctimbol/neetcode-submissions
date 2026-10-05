class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict from sorted str -> list of anagrams

        str_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))

            str_map[sorted_word].append(word)
        
        return list(str_map.values())