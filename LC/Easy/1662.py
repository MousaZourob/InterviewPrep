class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def generate(word):
            for w in word:
                for c in w:
                    yield c
            yield None
            
        for c1, c2 in zip(generate(word1), generate(word2)):
            if c1 != c2:
                return False
        return True