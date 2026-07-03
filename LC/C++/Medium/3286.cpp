class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        int m = grid.size();
        int n = grid[0].size();

        std::vector<std::vector<int>> dist(m, vector<int>(n, INT_MAX));
        dist[0][0] = grid[0][0];


        std::deque<std::pair<int, int>> dq{};
        dq.emplace_front(0, 0);

        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();

            for (auto [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;

                int nd = dist[r][c] + grid[nr][nc];
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    if (grid[nr][nc] == 1) dq.emplace_back(nr, nc);
                    else dq.emplace_front(nr, nc);
                }
            }
        }

        return dist[m - 1][n - 1] < health;
    }
};