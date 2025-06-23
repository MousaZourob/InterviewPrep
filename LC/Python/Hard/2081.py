class Solution:
    def is_palindrome(self, curr: int, k: int) -> bool:
            digit = list()
            while curr:
                digit.append(curr % k)
                curr //= k
            return digit == digit[::-1]

    def kMirror(self, k: int, n: int) -> int:
        ans = 0
        count = 0
        l = 1

        while count < n:
            r = l  * 10
            for op in [0, 1]:
                for i in range(l, r):
                    if count == n:
                        break
                    
                    curr = i
                    part = i if op == 1 else i // 10
                    while part:
                        curr = curr * 10 + part % 10
                        part //= 10
                    if self.is_palindrome(curr, k):
                        count += 1
                        ans += curr
            l = r

        return ans