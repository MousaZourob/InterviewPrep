class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        ans = []
        
        for c in s:
            if ans and abs(ord(c) - ord(ans[-1])) == 32:
                ans.pop()
            else:
                ans.append(c)

        return "".join(ans)