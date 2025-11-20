class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda i: (i[1], -i[0]))
        p1 = -1
        p2 = -1

        for s, e in intervals:
            if p2 < s:
                ans += 2
                p1 = e - 1
                p2 = e
            elif p1 < s:
                ans += 1
                p1 = p2
                p2 = e
        
        return ans
