class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        std::vector<int> furthestReach(n + 1, 0);
        for (int i = 0; i < ranges.size(); ++i) {
            int left = std::max(0, i - ranges[i]);
            int right = std::min(n, i + ranges[i]);
            furthestReach[left] = std::max(furthestReach[left], right);
        }

        int wateredUpTo = 0;
        int furthest = 0;
        int ans = 0;

        for (int i = 0; i < n; ++i) {
            furthest = std::max(furthest, furthestReach[i]);
            if (i == wateredUpTo) {
                if (i == furthest) return -1;
                ans++;
                wateredUpTo = furthest;
            }
        }

        return ans;
    }
};