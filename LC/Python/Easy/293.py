class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        ans = []
        
        for i in range(n-1):
            if currentState[i] == '+' and currentState[i+1] == '+':
                new_state = currentState[:i] + "--" + currentState[i+2:]
                ans.append(new_state)
        
        return ans