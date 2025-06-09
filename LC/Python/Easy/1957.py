class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0]]
        curr = s[0]
        count = 1
        for c in s[1:]:
            if c == curr:
                count += 1
            else:
                count = 1
                curr = c
            if count < 3:
                ans.append(c)
                
        return ''.join(ans)