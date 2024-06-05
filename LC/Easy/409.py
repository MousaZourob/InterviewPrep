class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
            
            if count[c] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        
        if odd_count > 0:
            return len(s) - odd_count + 1
        else:
            return len(s)