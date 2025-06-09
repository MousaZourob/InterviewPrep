class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        translate = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        
        for word in words:
            translation = ""
            for c in word:
                translation += translate[ord(c)-ord('a')]
            
            ans.add(translation)
            
        return len(ans)