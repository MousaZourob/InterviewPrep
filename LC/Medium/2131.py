class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        word_count = defaultdict(int)
        
        for word in words:
            if word_count[word[::-1]]:
                ans += 4
                word_count[word[::-1]] -= 1
            else:
                word_count[word] += 1
        
        for word in word_count:
            if word[0] == word[1] and word_count[word] > 0:
                ans += 2
                break
        
        return ans