class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for i in range(0, len(word)):
            if word[i] == '.':
                for candidate in curr:
                    if candidate == '*':
                        continue
                    new_word = word[0:i] + candidate + word[i+1:len(word)]
                    if self.search(new_word):
                        return True
                return False
            
            elif word[i] not in curr:
                return False
            curr = curr[word[i]]
       
        if not curr.get('*'):
            return False
        return True

            
