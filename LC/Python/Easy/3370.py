class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**int(log2(n)+1) - 1
