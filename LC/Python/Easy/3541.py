class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        max_vowels = 0
        max_consonant = 0

        for k,v in count.items():
            if k in ['a', 'e', 'i', 'o','u']:
                max_vowels = max(max_vowels, v)
            else:
                max_consonant = max(max_consonant, v)

        return max_vowels + max_consonant