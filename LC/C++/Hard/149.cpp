class Solution {
public:
    double calculateSlope(vector<int> p1, vector<int> p2) {
        double x1 = p1[0], y1 = p1[1];
        double x2 = p2[0], y2 = p2[1];

        if (x1 == x2) return DBL_MAX;
        if (y1 == y2) return 0;

        return (y2 - y1) / (x2 - x1);
    }

    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 1) { return 1; }

        int ans = 0;

        for (int i = 0; i < n; ++i) {
            std::unordered_map<double, int> count;
            for (int j = i + 1; j < n; ++j) {
                double slope = calculateSlope(points[i], points[j]);
                count[slope] += 1;
                ans = max(ans, count[slope]);
            }
        }

        return ans + 1;
    }
};