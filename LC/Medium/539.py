class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
        minutes.sort()
        ans = inf
        for i in range(len(minutes)-1):
            ans = min(ans, minutes[i+1] - minutes[i])
        
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])