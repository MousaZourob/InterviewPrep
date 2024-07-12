class Solution:
    def reverseParentheses(self, s: str) -> str:
        parans = deque()
        ans = []

        for c in s:
            if c == "(":
                parans.append(len(ans))
            elif c == ")":
                start = parans.pop()
                ans[start:] = ans[start:][::-1]
            else:
                ans.append(c)

        return "".join(ans)