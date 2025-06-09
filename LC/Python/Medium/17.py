class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_lett = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        ans = []
        
        curr = []
        def dfs(i):
            if len(digits) == len(curr):
                ans.append("".join(curr))
                return
            
            for c in num_lett[digits[i]]:
                curr.append(c)
                dfs(i + 1,)
                curr.pop()
            
        if digits:
            dfs(0)
        
        return ans