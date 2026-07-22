class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        letterMap = {2: ['a','b','c'],
                     3: ['d','e','f'],
                     4: ['g','h','i'],
                     5: ['j','k','l'],
                     6: ['m','n','o'],
                     7: ['p','q','r','s'],
                     8: ['t','u','v'],
                     9: ['w','x','y','z']
                     }
        def backtrack(index,path):
            s = "".join(path)
            if len(path) == len(digits) and s!="" :
                results.append(s)
            elif len(path)> len(digits):
                return

            for i in range(index, len(digits)):
                for z in letterMap[int(digits[i])]:
                    path.append(z)
                    backtrack(i+1, path)
                    path.pop()
            
        backtrack(0,[])
        return results
        


        