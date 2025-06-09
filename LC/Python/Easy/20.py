class Solution:
    def isValid(self, s: str) -> bool:
        valid_combs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        
        for c in s:
            if c in valid_combs:
                if stack and stack[-1] == valid_combs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0