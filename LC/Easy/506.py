class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []
        
        for i, s in enumerate(score):
            heappush(heap, (-s, i))
        
        ans = [-1] * n
        place = 1
        while heap:
            curr = heappop(heap)[1]
            if place == 1:
                ans[curr] = "Gold Medal"
            elif place == 2:
                ans[curr] = "Silver Medal"
            elif place == 3:
                ans[curr] = "Bronze Medal"
            else:
                ans[curr] = str(place)
            place += 1
        
        return ans
        