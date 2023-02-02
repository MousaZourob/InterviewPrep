class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {k: v for v, k in enumerate(order)}
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if len(words[i+1]) < j+1 or index[words[i][j]] > index[words[i+1][j]]:
                    return False
                elif index[words[i][j]] < index[words[i+1][j]]:
                    break
                    
        return True