class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        
        for i, word in enumerate(sentence):
            found = True
            for j in range(len(searchWord)):
                if j >= len(word) or word[j] != searchWord[j]:
                    found = False
                    break
            
            if found:
                return i + 1
        
        
        return -1