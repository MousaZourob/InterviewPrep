from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        count = Counter(s)
        stack = []
        min_char = 'a'
        for c in s:
            stack.append(c)
            count[c] -= 1
            while min_char != 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            while stack and stack[-1] <= min_char:
                ans.append(stack.pop())

        return ''.join(ans)
