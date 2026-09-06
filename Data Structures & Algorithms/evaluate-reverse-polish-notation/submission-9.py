class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if token == '+':
                    stack.append(str(val1+val2))
                elif token == '-':
                    stack.append(str(val1-val2))
                elif token == '*':
                    stack.append(str(val1*val2))
                else:
                     stack.append(str(int(val1/val2)))
            else:
                stack.append(token)
        
        return int(stack.pop())