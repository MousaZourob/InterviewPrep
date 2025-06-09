class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0] * 26
        n = len(words)
        
        for word in words:
            for c in word:
                count[ord(c) - ord('a')] += 1
        
        for c in count:
            if c % n != 0:
                return False
        
        return True