class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 10**7):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i
        
        return 0