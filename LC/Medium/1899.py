class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1 = t2 = t3 = 0
        
        for e1, e2, e3 in triplets:
            if e1 > target[0] or e2 > target[1] or e3 > target[2]:
                continue
            else:
                t1 = max(t1, e1)
                t2 = max(t2, e2)
                t3 = max(t3, e3)
        
        return [t1, t2, t3] == target