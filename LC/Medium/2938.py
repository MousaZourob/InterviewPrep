class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zeros = 0
        
        for c in s[::-1]:
            if c == '0':
                zeros += 1
            else:
                ans += zeros
        return ans