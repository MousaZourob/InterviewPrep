class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        i, j, n = 0, 1, len(word)
        while j < n:
            k = 0
            while j + k < n and word[i + k] == word[j + k]:
                k += 1
            if j + k < n and word[i + k] < word[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        last = word[i:]
        n, m = len(word), len(last)
        return last[: min(m, n - numFriends + 1)]