class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start,end in intervals:
            if heap and start > heap[0]:
                heappop(heap)
            
            heappush(heap, end)
            
        return len(heap)