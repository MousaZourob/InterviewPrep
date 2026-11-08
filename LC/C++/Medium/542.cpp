class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();        std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        std::queue<std::pair<int, int>> q;

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (mat[r][c] == 0) {
                    q.emplace(r, c);
                } else {
                    mat[r][c] = -1;
                }
            }
        }

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            for (auto& [x, y] : dirs) {
                int nr = r + x;
                int nc = c + y;

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                if (mat[nr][nc] != -1) {
                    continue;
                }

                mat[nr][nc] = mat[r][c] + 1;
                q.emplace(nr, nc);
            }
        }

        return mat;
    }
};