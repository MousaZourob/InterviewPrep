class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        
        for t0, t1, t2 in triplets:
            if t0 > target[0] or t1 > target[1] or t2 > target[2]:
                continue
            
            res[0] = max(res[0], t0)
            res[1] = max(res[1], t1)
            res[2] = max(res[2], t2)
        
        return res == target