class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = [int(x) for x in v1.split(".")], [int(x) for x in v2.split(".")]
        
        i = 0
        while i < len(v1) or i < len(v2):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            
            if a > b:
                return 1
            if a < b:
                return -1
            i += 1
        return 0