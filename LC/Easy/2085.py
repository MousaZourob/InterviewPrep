class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_count = Counter(words1)
        words2_count = Counter(words2)
        ans = 0
        
        for word in words1:
            if words1_count[word] == 1 and words2_count[word] == 1:
                ans += 1
            
        return ans