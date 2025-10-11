class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = -inf

        for i in range(n-k, n):
            curr = 0
            j = i
            while j >= 0:
                curr += energy[j]
                ans = max(ans, curr)
                j -= k

        return ans