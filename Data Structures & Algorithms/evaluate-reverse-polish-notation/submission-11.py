class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                if token == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif token == '-':
                    val2 = int(stack.pop())
                    stack.append(int(stack.pop()) - val2)
                elif token == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    val2 = int(stack.pop())
                    stack.append(int(stack.pop()) / val2)
            else:
                stack.append(token)
        return int(stack[0])
