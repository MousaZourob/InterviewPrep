class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        seen_characters = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(s)):
            rc = s[r]
            seen_characters[rc] += 1

            while k < len(seen_characters):
                lc = s[l]
                seen_characters[lc] -= 1
                if seen_characters[lc] == 0:
                    del seen_characters[lc]
                l += 1

            ans = max(ans, r-l + 1)

        return ans