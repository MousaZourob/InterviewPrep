class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int x = 0;
        int y = 0;
        int dirr = 0;
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        std::set<pair<int, int>> obs{};
        for (auto& ob : obstacles) {
            obs.insert({ob[0], ob[1]});
        }
        int ans = 0;
        for (int c : commands) {
            if (c == -1) {
                dirr = (dirr + 1) % 4;
            } else if (c == -2) {
                dirr = (dirr + 3) % 4;
            } else {
                for (int i = 0; i < c; i++) {
                    if (obs.count({x + dx[dirr], y + dy[dirr]})) break;

                    x += dx[dirr];
                    y += dy[dirr];
                }
                ans = max(ans, x*x + y*y);
            }
        }
        return ans;
    }
};