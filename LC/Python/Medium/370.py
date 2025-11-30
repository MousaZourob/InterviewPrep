class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        ranges = [0] * length
        for s, e, amt in updates:
            ranges[s] += amt
            if e < length - 1:
                ranges[e+1] -= amt

        curr = 0
        for i, r in enumerate(ranges):
            curr += r
            ans[i] = curr

        return ans
