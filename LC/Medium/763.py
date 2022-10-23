class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        ans = []

        curr_length = 0
        curr_letters = []

        for c in s:
            if c not in curr_letters:
                curr_letters.append(c)

            count[c] -= 1
            curr_length += 1

            if count[c] == 0:
                curr_letters.remove(c)

            if not curr_letters:
                ans.append(curr_length)
                curr_length = 0
                curr_letters = []

        return ans