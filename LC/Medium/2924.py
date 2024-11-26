class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degrees = [0] * n
        for a, b in edges:
            in_degrees[b] = 1
        
        sources = [n for n in range(n) if in_degrees[n] == 0] 

        return sources[0] if len(sources) == 1 else -1