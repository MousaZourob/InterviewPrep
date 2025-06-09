class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        
        winstreak = 0
        winner = arr[0]
        
        for i in range(1, len(arr)):
            opponent = arr[i]
            if winner > opponent:
                winstreak += 1
            else:
                winner = opponent
                winstreak = 1
                
            if winstreak == k:
                break
        
        return winner