class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = set([1])
        
        curr = 1
        for i in range(n):
            curr = min(ans)
            ans.remove(curr)
            ans.add(curr*2)
            ans.add(curr*3)
            ans.add(curr*5)
        
        return curr