class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heappush(heap, (arr[i]/arr[j], arr[i], arr[j]))
        
        while k > 1:
            heappop(heap)
            k -= 1

        return [heap[0][1], heap[0][2]]