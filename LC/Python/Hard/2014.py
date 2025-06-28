class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        freq = Counter(s)
        candidates = sorted(
            [c for c, w in freq.items() if w >= k], reverse = True
        )
        q = deque(candidates)

        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr

            for c in candidates:
                nxt = curr + c
                it = iter(s)
                if all(c in it for c in nxt*k):
                    q.append(nxt)

        return ans