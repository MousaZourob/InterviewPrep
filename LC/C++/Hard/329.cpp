class Solution {
    int m, n;
    vector<vector<int>> cache;
    vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    int dfs(vector<vector<int>>& matrix, int r, int c) {
        if (cache[r][c] != -1) {
            return cache[r][c];
        }

        int res = 0;

        for (auto [dr, dc] : dirs) {
            int nr = r + dr;
            int nc = c + dc;

            if (nr >= 0 && nr < m && nc >= 0 && nc < n && matrix[r][c] < matrix[nr][nc]) {
                res = max(res, 1 + dfs(matrix, nr, nc));
            }
        }

        return cache[r][c] = res;
    }

public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();
        cache.assign(m, vector<int>(n, -1));

        int ans = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans = max(ans, 1 + dfs(matrix, i, j));
            }
        }

        return ans;
    }
};