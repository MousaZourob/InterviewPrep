class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(),
            [](const auto& a, const auto& b) {
                return a[0] == b[0] ? b[1] < a[1] : a[0] < b[0];
            }
        );

        int ans = 0;
        int end, prev_end = 0;
        for (auto& interval : intervals) {
            end = interval[1];

            if (prev_end < end) {
                ans++;
                prev_end = end;
            }
        }

        return ans;
    }
};