import math
from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        diffs = [stations[i] - stations[i-1] for i in range(1, (len(stations)))]
        l = 0
        r = max(diffs)

        while r - l > 10**-6:
            m = r + (l - r) / 2
            needed = 0
            for diff in diffs:
                needed += ceil(diff / m) - 1
                if needed > k:
                    break

            if needed <= k:
                r = m
            else:
                l = m
        
        return r
