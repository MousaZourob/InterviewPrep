class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        
        def generate_brackets(o_brackets, c_brackets):
            if o_brackets == c_brackets == n:
                ans.append("".join(stack))
            elif o_brackets == c_brackets:
                stack.append("(")
                generate_brackets(o_brackets+1, c_brackets)
                stack.pop()
            elif o_brackets == n:
                stack.append(")")
                generate_brackets(o_brackets, c_brackets+1)
                stack.pop()
            else:
                stack.append("(")
                generate_brackets(o_brackets+1, c_brackets)
                stack.pop()
                
                stack.append(")")
                generate_brackets(o_brackets, c_brackets+1)
                stack.pop()
                
        generate_brackets(0, 0)
        return ans