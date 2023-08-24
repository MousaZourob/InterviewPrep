class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)
        prev = None

        while heap or prev:
            if prev and not heap:
                return ""
            
            c, char = heappop(heap)
            ans.append(char)
            c += 1
            
            if prev:
                heappush(heap, prev)
                prev = None
            if c != 0:
                prev = (c, char)
            
        return ''.join(ans)