class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        
        for i in range(n):
            dist[i] = ceil(dist[i] / speed[i])
            speed[i] = 0
            
        for arrive in dist:
            if arrive >= n:
                continue
            speed[arrive] += 1
        
        for i in range(1, n):
            speed[i] += speed[i-1]
            
            if speed[i] > i:
                return i
        
        return n