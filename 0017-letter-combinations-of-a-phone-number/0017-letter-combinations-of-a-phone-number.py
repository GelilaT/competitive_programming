class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letter = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
        ans = []
        def backtrack(path, idx):
            
            if len(path) == len(digits):
                if path:
                    ans.append("".join(path))
                return

            for i in range(idx, len(digits)):
                for j in letter[digits[i]]:
                    path.append(j)
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)
        return ans                    
