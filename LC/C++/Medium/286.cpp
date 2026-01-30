class Solution {
    using State = pair<int, int>;
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size();
        int n = rooms[0].size();
        vector<State> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        std::queue<State> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (rooms[i][j] == 0) {
                    q.emplace(i, j);
                }
            }
        }

        std::set<State> visited;
        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            
            for (auto& [dx, dy] : dirs) {
                int nx = x + dx;
                int ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && rooms[nx][ny] != -1 && rooms[nx][ny] == 2147483647) {
                    rooms[nx][ny] = rooms[x][y] + 1;
                    q.emplace(nx, ny);
                }
            }

        }
    }
};
