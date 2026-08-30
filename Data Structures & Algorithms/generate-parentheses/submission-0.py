class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # not valid:
            # num '(' > n OR num ')' > num '('

        pars = []

        def backtrack(current, open, close, pars):
            print(current)
            if open == close == n:
                print(''.join(current))
                pars.append(''.join(current))
                return

            if open < n:
                backtrack(current + ['('], open+1, close, pars)
            if open > close:
                backtrack(current + [')'], open, close+1, pars)
            
        
        backtrack([], 0, 0, pars)

        return pars