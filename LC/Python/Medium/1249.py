class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = list(s)
        stack = []
        
        for i in range(len(ans)):
            if ans[i] == '(':
                stack.append(i)
            elif ans[i] == ')':
                if stack:
                    stack.pop()
                else:
                    ans[i] = ""
        
        for i in stack:
            ans[i] = ""
        
        return ''.join(ans)
                