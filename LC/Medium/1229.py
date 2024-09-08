class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        i, j = 0, 0
        
        while i < len(slots1) and j < len(slots2):
            if slots1[i][0] <= slots2[j][0] < slots1[i][1] or slots2[j][0] <= slots1[i][0] < slots2[j][1]:
                if min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0]) >= duration:
                    return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0])+duration]
            
            if slots1[i][1] >= slots2[j][1]:
                j += 1
            else:
                i += 1
            
        return []