class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        ans = 0
        for child in g[::-1]:
            if not s:
                break
            if child <= s[-1]:
                ans += 1
                s.pop()
        
        return ans