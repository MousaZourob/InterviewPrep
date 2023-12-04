class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = '-1'

        for i in range(len(num)-2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, num[i])
            
        return '' if ans == '-1' else ans*3