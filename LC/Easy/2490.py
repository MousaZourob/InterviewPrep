class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if len(sentence) == 0: return True
        sentence = sentence.split()
        sentence.append(sentence[0])
        
        for i in range(len(sentence) - 1):
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        
        return True