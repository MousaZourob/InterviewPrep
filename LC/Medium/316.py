class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        last_occurance = {}
        
        for i, c in enumerate(s):
            last_occurance[c] = i
            
        for i, c in enumerate(s):
            if c not in ans:
                while ans and i < last_occurance[ans[-1]] and c < ans[-1]:
                    ans.pop()
                ans.append(c)
        
        return ''.join(ans)