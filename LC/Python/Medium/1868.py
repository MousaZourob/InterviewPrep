class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]
            
            prod = val1*val2
            freq = min(freq1, freq2)
            
            if not ans or prod != ans[-1][0]:
                ans.append([prod, freq])
            else:
                ans[-1][1] += freq
                
            encoded1[i][1] -= freq
            if freq1 == freq:
                i += 1
            
            encoded2[j][1] -= freq
            if freq2 == freq:
                j += 1
            
        return ans
            