class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                
                if t == "+":
                    curr = n2+n1
                elif t == "-":
                    curr = n2-n1
                elif t == "*":
                    curr = n2*n1
                else:
                    curr = int(float(n2)/n1)
                stack.append(curr)
                
        return stack[0]