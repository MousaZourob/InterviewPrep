class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size();
        int n = maze[0].size();
        std::vector<std::pair<int,int>> dirs {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        std::queue<std::pair<int, int>> q;
        std::set<std::pair<int, int>> visited;
        q.emplace(start[0], start[1]);

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            if (r == destination[0] && c == destination[1]) {
                return true;
            }

            for (auto& [x, y] : dirs) {
                int nr = r + x, nc = c + y;
                while ((nr >= 0 && nr < m) && (nc >= 0 && nc < n) && maze[nr][nc] != 1) {
                    nr += x;
                    nc += y;
                }
                nr -= x;
                nc -= y;

                if (!visited.contains({nr, nc})) {
                    visited.insert({nr, nc});
                    q.emplace(nr, nc);
                }

            }
        }

        return false;
    }
};