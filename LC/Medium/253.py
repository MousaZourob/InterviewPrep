class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        ans = 0
        e = 0
        
        for s in range(len(start)):
            if start[s] < end[e]:
                ans += 1
            else:
                e += 1
        
        return ans