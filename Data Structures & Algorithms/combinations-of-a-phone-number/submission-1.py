class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backtrack(path, position):
            print(path)
            if position == len(digits):
                path_copy = path[:]
                if path_copy:
                    res.append("".join(path_copy))
                return

            for i in range(len(keypad[digits[position]])):
                chars = keypad[digits[position]]
                path.append(chars[i])
                backtrack(path, position+1)
                path.pop()
            return
        backtrack([], 0)
        return res
            