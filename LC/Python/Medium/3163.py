class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        prev = word[0]
        count = 1
        for c in word[1:]:
            if c == prev and count < 9:
                count += 1
            else:
                ans.append(str(count))
                ans.append(prev)
                count = 1
                prev = c
            
        ans.append(str(count))
        ans.append(prev)
        return ''.join(ans)