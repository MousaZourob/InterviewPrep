class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        counted_ones = 0

        for i, c in enumerate(s):

            if c == '1':
                counted_ones +=1

            else:
                if i > 0 and s[i-1] == '1':
                    ans += counted_ones

        return ans
