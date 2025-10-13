class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = [words[0]]

        def compare(word1, word2):
            count = [0] * 26
            for c in word1:
                count[ord(c) - ord('a')] += 1
            for c in word2:
                count[ord(c) - ord('a')] -= 1
            return all(x == 0 for x in count)

        for i in range(1, n):
            if compare(words[i-1], words[i]):
                continue
            ans.append(words[i])
        return ans