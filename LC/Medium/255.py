class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        parent = -inf
        stack = []
        
        for n in preorder:
            while stack and stack[-1] < n:
                parent = stack.pop()
            
            if n <= parent:
                return False
            
            stack.append(n)
        
        return True