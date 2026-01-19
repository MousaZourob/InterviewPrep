class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size();
        int n = maze[0].size();

        vector<vector<int>> distance(m, vector<int>(n, numeric_limits<int>::max()));
        distance[start[0]][start[1]] = 0;
    
        dijkstra(maze, start, distance);

        return distance[destination[0]][destination[1]] == numeric_limits<int>::max() ? -1 : distance[destination[0]][destination[1]];
    }
private:
    void dijkstra(const vector<vector<int>>& maze, const vector<int>& start, vector<vector<int>>& distance) {
        int m = maze.size();
        int n = maze[0].size();
        const vector<pair<int,int>> directions = {{0,1}, {0,-1}, {-1,0}, {1,0}};
        using State = tuple<int, int, int>;

        std::priority_queue<State, vector<State>, greater<>> pq;
        pq.push({0, start[0], start[1]});

        while (!pq.empty()) {
            auto [dist, x, y] = pq.top();
            pq.pop();

            if (distance[x][y] < dist) {
                continue;
            }

            for (auto [dx, dy] : directions) {
                int nx = x, ny = y, dist = 0;
                while (
                    (nx + dx >= 0 && nx + dx < m) && 
                    (ny + dy >= 0 && ny + dy < n) &&
                    maze[nx+dx][ny+dy] == 0
                    ) 
                    {
                        nx += dx;
                        ny += dy;
                        ++dist;
                    }
                
                if (distance[x][y] + dist < distance[nx][ny]) {
                    distance[nx][ny] = distance[x][y] + dist;
                    pq.emplace(distance[nx][ny], nx, ny);
                }
            }

        }
    }
};