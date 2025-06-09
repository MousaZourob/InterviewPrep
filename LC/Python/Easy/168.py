class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        
        while columnNumber:
            columnNumber -= 1
            rem = columnNumber % 26
            ans.append(chr(65+rem))
            columnNumber = columnNumber // 26
            
        return ''.join(reversed(ans))