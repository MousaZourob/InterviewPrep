class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        ans = len(word)
        for i in count.values():
            deleted = 0
            for j in count.values():
                if i > j:
                    deleted += j
                elif j > i + k:
                    deleted += j - i - k
            ans = min(ans, deleted)
        
        return ans
