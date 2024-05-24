class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        lcount = Counter(letters)
        
        def can_form(w):
            wcount = Counter(w)
            for c in w:
                if wcount[c] > lcount[c]:
                    return False
            return True
        
        def get_score(w):
            res = 0
            for c in w:
                res += score[ord(c)-ord('a')]
            return res
        
        def dfs(i):
            if i >= n:
                return 0
            res = dfs(i+1)
            
            if can_form(words[i]):
                for c in words[i]:
                    lcount[c] -= 1
                res = max(res, get_score(words[i]) + dfs(i+1))
                for c in words[i]:
                    lcount[c] += 1
            return res
        
        return dfs(0)