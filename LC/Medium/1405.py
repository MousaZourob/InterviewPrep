class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))
        ans = []
        
        while heap:
            c, char = heappop(heap)
            
            if len(ans) > 1 and ans[-2] == ans[-1] == char:
                if not heap:
                    break
                c2, char2 = heappop(heap)
                c2 += 1
                ans.append(char2)
                if c2:
                    heappush(heap, (c2, char2))
            else:
                c += 1
                ans.append(char)
            if c:
                heappush(heap, (c, char))
            
        return "".join(ans)
            