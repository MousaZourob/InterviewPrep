class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack1 = []
        pair = 'ab' if x > y else 'ba'
        ans = 0
        
        for c in s:
            if c == pair[1] and stack1 and stack1[-1] == pair[0]:
                stack1.pop()
                ans += max(x,y)
            else:
                stack1.append(c)

        stack2 = []
        for c in stack1:
            if c == pair[0] and stack2 and stack2[-1] == pair[1]:
                stack2.pop()
                ans += min(x,y)
            else:
                stack2.append(c)
            
        return ans