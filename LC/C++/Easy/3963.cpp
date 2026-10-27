class Solution {
public:
    vector<string> createGrid(int m, int n) {
        std::vector<std::string> ans(m, std::string(n, '#'));
    
        for (int i = 0; i < std::max(m, n); ++i) {
            if (i < m) ans[i][0] = '.';
            if (i < n) ans[m - 1][i] = '.';
        }

        return ans;
    }
};