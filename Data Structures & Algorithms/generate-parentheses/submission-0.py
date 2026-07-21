class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        options = ['(', ')']

        def isValidParenthesis(parenthesis: str):
            if parenthesis == '':
                return False
            imbalance = 0
            for bracket in parenthesis:
                if imbalance<0:
                    return False
                if bracket == '(':
                    imbalance +=1
                elif bracket == ')':
                    imbalance -=1
            if imbalance == 0 and len(parenthesis)==2*n:
                return True

        def backtrack(path):
            if n <0:
                return
            s = ''.join(path)
            if isValidParenthesis(s):
                results.append(s)
            if len(s)>2*n:
                return
            
            for i in range(2):
                path.append(options[i])
                backtrack(path)
                path.pop()
        backtrack([])
        return results




        