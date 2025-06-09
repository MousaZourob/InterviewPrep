class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def checkNeighbour(a, b):
            return sum(a[i] != b[i] for i in range(len(a))) == 1
        
        q = [(start, 0)]
        seen = {start}
        
        while q:
            curr, ans = q.pop(0)
            
            if curr == end:
                return ans
            
            for neighbour in bank:
                if neighbour not in seen and checkNeighbour(curr, neighbour):
                    q.append((neighbour, ans + 1))
                    seen.add(neighbour)
                    
        return -1