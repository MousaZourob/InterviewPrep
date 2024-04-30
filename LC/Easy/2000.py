class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word if not (i := word.find(ch) + 1) else word[:i][::-1] + word[i:]