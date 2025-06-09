class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = [float('inf')] * 26
        ans = []

        for s in words:
            count1 = [0] * 26
            for c in s:
                count1[ord(c) - ord('a')] += 1
            for i in range(26):
                count[i] = min(count[i], count1[i])

        for i in range(26):
            ans += [chr(i + ord('a'))] * count[i]

        return ans