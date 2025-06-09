class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        l = 0
        r = len(s) - 1
        s = list(s)
        
        while r > l:
            if s[r] in vowels and s[l] in vowels:
                s[l], s[r] = s[r], s[l]
                r -= 1
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] not in vowels:
                l += 1
                
        return "".join(s)