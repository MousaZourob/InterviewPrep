class Solution {
    int m;
    int n;
    std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    bool dfs(vector<vector<int>>& grid, int r, int c) {
        grid[r][c] = 1;

        bool res = !(r == 0 || r == m - 1 || c == 0 || c == n - 1);

        for (auto& [x, y] : dirs) {
            int nr = r + x;
            int nc = c + y;

            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 1) {
                continue;
            }

            bool childClosed = dfs(grid, nr, nc);
            res = res && childClosed;
        }

        return res;
    }

public:
    int closedIsland(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        int ans{};

        for (int i = 1; i < m-1; ++i) {
            for (int j = 1; j < n-1; ++j) {
                if (grid[i][j] == 0 && dfs(grid, i, j)) {
                    ans++;
                }
            }
        }

        return ans;
    }
};