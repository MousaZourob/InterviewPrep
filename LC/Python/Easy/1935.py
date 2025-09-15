class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        letters_set = set(brokenLetters)

        count = 0
        for word in words:
            for c in word:
                if c in letters_set:
                    count += 1
                    break
        return len(words) - count