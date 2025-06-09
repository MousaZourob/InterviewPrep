class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        
        for char in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                onTrue = stack.pop()
                stack.pop()
                onFalse = stack.pop()
                stack.append(onTrue if char == 'T' else onFalse)
            else:
                stack.append(char)
        
        # Return the final character
        return stack[0]