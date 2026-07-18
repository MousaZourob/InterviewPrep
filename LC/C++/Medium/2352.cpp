class Solution {
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            size_t hash = 0;
            for (int x : v)
                hash ^= std::hash<int>{}(x) + 0x9e3779b9 + (hash << 6) + (hash >> 2);
            return hash;
        }
    };

public:
    int equalPairs(vector<vector<int>>& grid) {
        unordered_map<vector<int>, int, VectorHash> rows;
        
        for (auto row : grid) {
            rows[row]++;
        }

        int ans = 0;
        for (int i = 0; i < grid.size(); ++i) {
            std::vector<int> c{};
            for (int j = 0; j < grid.size(); ++j) {
                c.push_back(grid[j][i]);
            }
            ans += rows[c];
        }

        return ans;
    }
};