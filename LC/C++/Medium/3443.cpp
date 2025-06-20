class Solution {
public:
    int maxDistance(string s, int k) {
        int north = 0;
        int south = 0;
        int east = 0;
        int west = 0;
        int ans = 0;

        for (auto &c : s) {
            if (c == 'N') {
                north++;
            } else if (c == 'S') {
                south++;
            } else if (c == 'E') {
                east++;
            } else if (c == 'W') {
                west++;
            }

            int vertical_changes = min(min(north, south), k);
            int horizontal_changes = min(min(east, west), k - vertical_changes);

            int vertical_distance = abs(north - south) + vertical_changes * 2;
            int horizontal_distance = abs(east - west) + horizontal_changes * 2;

            ans = max(ans, vertical_distance + horizontal_distance);
        }

        return ans;
    }
};