class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0
        
        for word in words:
            word_count = Counter(word)
            can_create_word = True
            
            for char in word:
                if chars_count[char] < word_count[char]:
                    can_create_word = False
                    break
                    
            if can_create_word:
                ans += len(word)
                
        return ans