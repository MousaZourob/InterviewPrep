class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = { 1: 0 }
        def get_power(n):
            if n in cache:
                return cache[n]
            elif n % 2 == 0:
                return 1 + get_power(n // 2)
            else:
                return 1 + get_power(n*3 + 1)
        
        heap = []
        
        for num in range(lo, hi + 1):
            power = get_power(num)
            heappush(heap, (power, num))
        
        heapify(heap)
        for _ in range(k-1):
            heappop(heap)
            
        return heap[0][1]