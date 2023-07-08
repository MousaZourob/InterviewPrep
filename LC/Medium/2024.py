class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        window_start = 0
        ans = k
        count = Counter(answerKey[:k])
        
        for window_end in range(k, len(answerKey)):
            count[answerKey[window_end]] += 1

            while min(count['T'], count['F']) > k:
                count[answerKey[window_start]] -= 1
                window_start += 1
                
            ans = max(ans, window_end - window_start + 1)
                
        return ans