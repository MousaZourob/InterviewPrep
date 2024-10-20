class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def eval_expr(op, vals):
            if op == '!':
                return 't' if vals[0] == 'f' else 'f'
            
            if op == '|':
                for val in vals:
                    if val == 't':
                        return 't'
                return 'f'
            
            if op == '&':
                for val in vals:
                    if val == 'f':
                        return 'f'
                return 't'
        
        stack = []
        
        for c in expression:
            if c == ')':
                vals = []
                
                while stack[-1] != '(':
                    vals.append(stack.pop())
                stack.pop()
                op = stack.pop()
                
                res = eval_expr(op, vals)
                stack.append(res)
            elif c != ',':
                stack.append(c)
    
        return stack[0] == 't'