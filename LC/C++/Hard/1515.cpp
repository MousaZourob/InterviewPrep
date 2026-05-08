class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        double x = 0;
        double y = 0;
        for (auto p : positions) {
            x += p[0];
            y += p[1];
        }
        x /= positions.size();
        y /= positions.size();
        auto cost = [&](double px, double py) -> double {
            double res = 0;
            for (auto p : positions) {
                res += sqrt(
                    (px - p[0]) * (px - p[0]) +
                    (py - p[1]) * (py - p[1])
                );
            }
            return res;
        };

        double ans = cost(x, y);
        double step = 100.0;

        vector<vector<int>> dirs{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        while (step > 1e-6) {
            bool improved = false;

            for (auto p : dirs) {
                double nx = x + p[0] * step;
                double ny = y + p[1] * step;
                double val = cost(nx, ny);

                if (val < ans) {
                    x = nx;
                    y = ny;

                    ans = val;
                    improved = true;
                    break;
                }
            }

            if (!improved) {
                step *= 0.5;
            }
        }

        return ans;
    }
};