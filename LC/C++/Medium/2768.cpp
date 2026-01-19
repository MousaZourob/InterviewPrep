class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        vector<long long> ans(5, 0);
        map<pair<int,int>, int> block_counts;
        const vector<pair<int,int>> dirs = {{0,0}, {0,-1}, {-1,0}, {-1,-1}};


        for (auto& p : coordinates) {
            int r = p[0], c = p[1];

            for (auto [x, y] : dirs) {
                int nr = r + x, nc = c + y;
                if (nr >= 0 && nc >= 0 && nr < m - 1 && nc < n - 1) {
                    block_counts[make_pair(nr, nc)]++;
                }
            }
        }

        ans[0] = (long long)(m - 1) * (n - 1) - block_counts.size();
        for (const auto& entry : block_counts) {
            ans[entry.second]++;
        }

        return ans;
    }
};