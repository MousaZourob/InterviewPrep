class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ans = []
        
        for c in s:
            if c not in vowels:
                ans.append(c)
            
        return ''.join(ans)