class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Sort both lists in ascending order
        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_width = max(verticalCuts[0], w - verticalCuts[-1])

        # Find maximum difference of neighbors of horizontal_bars
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        # Find maximum difference of neighbors of vertical_bars
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        # Print the largest area
        return (max_height * max_width) % (10**9 + 7)


