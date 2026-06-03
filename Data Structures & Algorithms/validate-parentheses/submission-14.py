class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPar = ["(", "[", "{"]
        closePar = [")", "]", "}"]

        for i in range(0, len(s)):
            if s[i] in openPar:
                stack.append(s[i])
            elif stack and openPar.index(stack[-1]) == closePar.index(s[i]):
                stack.pop()
                continue
            else:
                return False
        return len(stack) == 0

