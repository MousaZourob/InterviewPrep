class Solution {
public:
    string findShortestWay(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
        int m = maze.size(), n = maze[0].size();

        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        vector<vector<string>> path(m, vector<string>(n, "~"));

        using State = tuple<int, string, int, int>;
        priority_queue<State, vector<State>, greater<>> pq;

        dist[ball[0]][ball[1]] = 0;
        path[ball[0]][ball[1]] = "";
        pq.push({0, "", ball[0], ball[1]});

        vector<pair<int,int>> dirs = {{1,0},{0,-1},{0,1},{-1,0}};
        vector<string> dirc = {"d","l","r","u"};

        while (!pq.empty()) {
            auto [cd, cp, x, y] = pq.top();
            pq.pop();

            if (x == hole[0] && y == hole[1]) return cp;
            if (cd > dist[x][y] || cp > path[x][y]) continue;

            for (int i = 0; i < 4; i++) {
                int nx = x, ny = y, step = 0;

                while (true) {
                    int tx = nx + dirs[i].first;
                    int ty = ny + dirs[i].second;
                    if (tx < 0 || tx >= m || ty < 0 || ty >= n || maze[tx][ty] == 1) break;
                    nx = tx;
                    ny = ty;
                    step++;
                    if (nx == hole[0] && ny == hole[1]) break;
                }

                int nd = cd + step;
                string np = cp + dirc[i];

                if (nd < dist[nx][ny] || (nd == dist[nx][ny] && np < path[nx][ny])) {
                    dist[nx][ny] = nd;
                    path[nx][ny] = np;
                    pq.push({nd, np, nx, ny});
                }
            }
        }

        return "impossible";
    }
};
