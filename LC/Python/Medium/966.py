class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def vowel_word(word):
            return "".join('*' if c in "aeiou" else c for c in word)
        words = set(wordlist)
        words_cap = {}
        words_vowel = {}

        for word in wordlist:
            word_low = word.lower()
            words_cap.setdefault(word_low, word)
            words_vowel.setdefault(vowel_word(word_low), word)

        ans = []

        for word in queries:
            if word in words:
                ans.append(word)
                continue
            
            word_low = word.lower()
            if word_low in words_cap:
                ans.append(words_cap[word_low])
                continue
            
            word_vowel = vowel_word(word_low)
            if word_vowel in words_vowel:
                ans.append(words_vowel[word_vowel])
                continue
            ans.append("")

        return ans