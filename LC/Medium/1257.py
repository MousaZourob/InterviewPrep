class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {}
        for region in regions:
            for area in region[1:]:
                parents[area] = region[0]
        
        r1 = region1
        r2 = region2
        while r1 != r2:
            r1 = parents.get(r1, region2)
            r2 = parents.get(r2, region1)

        return r1