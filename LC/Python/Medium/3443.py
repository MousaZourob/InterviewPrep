class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        north = south = east = west = 0
        ans = 0

        for move in s:
            if move == "N":
                north += 1
            elif move == "S":
                south += 1
            elif move == "E":
                east += 1
            elif move == "W":
                west += 1

            vertical_changes = min(min(north, south), k)
            horizontal_changes = min(min(east, west), k - vertical_changes)

            vertical_distance = abs(north - south) + vertical_changes * 2
            horizontal_distance = abs(east - west) + horizontal_changes * 2

            ans = max(ans, vertical_distance + horizontal_distance)

        return ans
