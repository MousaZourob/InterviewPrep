class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        m = len(str1)
        n = len(str2)
        for i in range(m):
            if (j < n) and (
                str1[i] == str2[j] 
                or ord(str1[i]) + 1 == ord(str2[j]) 
                or ord(str1[i]) - 25 == ord(str2[j])):
                j += 1
        
        return j == n