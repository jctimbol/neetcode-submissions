class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        if not curr.get('*'):
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True