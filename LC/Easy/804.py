class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translate = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = []
        
        for word in words:
            translation = ""
            for c in word:
                translation += translate[ord(c)-ord('a')]
            
            ans.append(translation)
            
        return len(set(ans))