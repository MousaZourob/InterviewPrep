class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        mid = n//2
        
        ans = 0
        for i in range(n):
            if s[i] in vowels:
                ans += 1 if i < mid else -1
  
        return ans == 0