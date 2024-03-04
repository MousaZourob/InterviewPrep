class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        ans = 0
        l, r = 0, n - 1
        
        score = 0
        while r >= l:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                ans = max(ans, score)
            elif power < tokens[l] and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                return ans
        
        return ans