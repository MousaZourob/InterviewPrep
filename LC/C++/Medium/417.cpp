class Solution {
public:
    int m, n;
    vector<vector<int>> heights;

    void dfs(int r, int c, set<pair<int, int>>& reachable) {
        reachable.insert({r, c});
        vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for (auto [dx, dy] : dirs) {
            int nr = r + dx;
            int nc = c + dy;
            
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            if (reachable.count({nr, nc})) continue;
            if (heights[nr][nc] < heights[r][c]) continue;
            
            dfs(nr, nc, reachable);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& inputHeights) {
        heights = inputHeights;
        m = heights.size();
        n = heights.at(0).size();

        set<pair<int, int>> atlReachable;
        set<pair<int, int>> pacReachable;

        for (int i = 0; i < m; i++) {
            dfs(i, 0, pacReachable);
            dfs(i, n - 1, atlReachable);
        }

        for (int i = 0; i < n; i++) {
            dfs(0, i, pacReachable);
            dfs(m-1, i, atlReachable);
        }

        vector<vector<int>> result;
        for (auto& cell : pacReachable) {
            if (atlReachable.count(cell)) {
                result.push_back({cell.first, cell.second});
            }
        }

        return result;
    }
};