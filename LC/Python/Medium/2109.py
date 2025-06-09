class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        
        curr_space = 0
        for i, c in enumerate(s):
            if curr_space < len(spaces) and i == spaces[curr_space]:
                ans.append(' ')
                curr_space += 1
            ans.append(c)
            
        return ''. join(ans)