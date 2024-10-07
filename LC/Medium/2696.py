class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for c in s:
            if stack:
                if (stack[-1] == 'A' and c == 'B') or (stack[-1] == 'C' and c == 'D'):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return len(stack)
