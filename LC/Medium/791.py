class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []
        
        for c in order:
            if c in count:
                ans.append(c*count[c])
                del count[c]
        
        for c, v in count.items():
            ans.append(c*v)
        
        return ''.join(ans)