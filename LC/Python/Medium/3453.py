class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l = 0
        r = 10**9

        def helper(line):
            above = 0
            below = 0

            for x, y, l in squares:
                total = l*l

                if line <= y:
                    above += total
                elif line >= y + l:
                    below += total
                else:
                    aboveH = (y + l) - line
                    belowH = line - y
                    above += l * aboveH
                    below += l * belowH
            
            return above - below

        for _ in range(60):
            m = (l + r) / 2
            diff = helper(m)

            if diff > 0:
                l = m
            else:
                r = m

        return r
