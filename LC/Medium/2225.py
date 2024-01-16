class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = [-1] * 100001
        
        for winner, loser in matches:
            if players[winner] == -1:
                players[winner] = 0
            if players[loser] == -1:
                players[loser] = 0
            players[loser] += 1

        ans = [[], []]
        for i in range(1, 100001):
            if players[i] == 0:
                ans[0].append(i)
            elif players[i] == 1:
                ans[1].append(i)
            
        return ans