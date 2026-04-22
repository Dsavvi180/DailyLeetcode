class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = {'(':')', '{':'}','[':']'}
        matches = {'(':')', '{':'}','[':']',')':'(','}':'{',']':'['}
        unmatched = [s[0]]
        for bracket in s[1:]:
            if len(unmatched) == 0:
                unmatched.append(bracket)
            elif bracket == matches[unmatched[-1]]:
                if unmatched[-1] in openBracket:
                    unmatched.pop()
            else:
                unmatched.append(bracket)
        return len(unmatched)==0
        