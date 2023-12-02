class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target_letter_count = Counter(target)
        s_letter_count = Counter(s)
        ans = 1000
        
        for c in target:
            ans = min(ans, s_letter_count[c] // target_letter_count[c])
            
        return ans if ans != 1000 else 0