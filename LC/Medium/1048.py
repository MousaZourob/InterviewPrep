class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        chains = {}
        ans = 0
        
        for word in words:
            chains[word] = 1
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                if pre in chains:
                    chains[word] = max(chains[word], chains[pre] + 1)
            
            ans = max(ans, chains[word])
        
        return ans