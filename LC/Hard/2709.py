class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
    
    def find(self, i):
        p = self.parent[i]
            
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.count -= 1
    
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factors = {}
        
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factors:
                        uf.union(i, factors[f])
                    else:
                        factors[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
                
            if n > 1:
                if n in factors:
                    uf.union(i, factors[n])
                else:
                    factors[n] = i

        return uf.count == 1