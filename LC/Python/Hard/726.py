class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        stack = [defaultdict(int)]
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                curr_map = stack.pop()
                count = ""
                while i + 1 < n and formula[i+1].isdigit():
                    count += formula[i+1]
                    i += 1
                count = 1 if not count else int(count)
                
                prev_map = stack[-1]
                for element in curr_map:
                    prev_map[element] += (curr_map[element] * count)
                
            else:
                element = formula[i]
                count = ""
                if i + 1 < n and formula[i+1].islower():
                    element = formula[i:i+2]
                    i += 1
                while i + 1 < n and formula[i+1].isdigit():
                    count += formula[i+1]
                    i += 1
                count = 1 if not count else int(count)
                
                curr_map = stack[-1]
                curr_map[element] += count    
            i += 1 
        
        ans = []
        final_formula = stack.pop()
        for element, count in sorted(final_formula.items()):
            ans.append(element)
            if count != 1:
                ans.append(str(count))

        return "".join(ans)