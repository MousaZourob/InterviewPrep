class Solution {
    int m_, n_;
    std::vector<std::vector<std::vector<bool>>> visited_;
    int ans_ = INT_MAX;

    void dfs(int r, int c, int x, vector<vector<int>>& grid) {
        x ^= grid[r][c];

        if (r == m_ - 1 && c == n_ - 1) {
            ans_ = min(ans_, x);
            return;
        }

        if (visited_[r][c][x]) return;
        visited_[r][c][x] = true;

        if (r + 1 < m_) {
            dfs(r + 1, c, x, grid);
        }

        if (c + 1 < n_) {
            dfs(r, c + 1, x, grid);
        }
    }

public:
    int minCost(vector<vector<int>>& grid) {
        m_ = grid.size();
        n_ = grid[0].size();

        visited_.resize(
            m_, std::vector<std::vector<bool>>(n_, std::vector<bool>(1024, false))
        );

        dfs(0, 0, 0, grid);
        return ans_;
    }
};