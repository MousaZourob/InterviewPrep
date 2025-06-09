class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        vowel_count = 0

        for r in range(len(s)):
            if s[r] in vowels:
                vowel_count += 1
            if r - k >= 0 and s[r-k] in vowels:
                vowel_count -= 1
            ans = max(ans, vowel_count)
            
        return ans