class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        count = [[] for _ in range(26)]

        for i, c in enumerate(s):
            if c != '*':
                count[ord(c) - ord('a')].append(i)
            else:
                s[i] = ''
                for j in range(26):
                    if count[j]:
                        s[count[j].pop()] = ''
                        break
        return ''.join(s)