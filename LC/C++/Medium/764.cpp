class Solution {
public:
    int orderOfLargestPlusSign(int n, vector<vector<int>>& mines) {
        std::vector<std::vector<bool>> mineSet(n, std::vector<bool>(n, false));

        for (auto& mine : mines) {
            mineSet[mine[0]][mine[1]] = true;
        }

        std::vector<std::vector<int>> left(n, std::vector<int>(n, 0));
        for (int i{}; i < n; ++i) {
            for (int j{}; j < n; ++j) {
                left[i][j] = mineSet[i][j] 
                    ? 0 
                    : 1 + (j > 0 ? left[i][j - 1] : 0); 
            }
        }
        
        std::vector<std::vector<int>> right(n, std::vector<int>(n, 0));
        for (int i{n - 1}; i >= 0; --i) {
            for (int j{n - 1}; j >= 0; --j) {
                right[i][j] = mineSet[i][j] 
                    ? 0 
                    : 1 + (j < n - 1 ? right[i][j + 1] : 0); 
            }
        }

        std::vector<std::vector<int>> up(n, std::vector<int>(n, 0));
        for (int i{}; i < n; ++i) {
            for (int j{}; j < n; ++j) {
                up[i][j] = mineSet[i][j] 
                    ? 0 
                    : 1 + (i > 0 ? up[i - 1][j] : 0); 
            }
        }
        
        std::vector<std::vector<int>> down(n, std::vector<int>(n, 0));
        for (int i{n - 1}; i >= 0; --i) {
            for (int j{n - 1}; j >= 0; --j) {
                down[i][j] = mineSet[i][j] 
                    ? 0 
                    : 1 + (i < n - 1 ? down[i + 1][j] : 0);
            }
        }
        
        int ans = 0;
        for (int i{}; i < n; ++i) {
            for (int j{}; j < n; ++j) {
                ans = std::max(ans, std::min({left[i][j], right[i][j], up[i][j], down[i][j]}));
            }
        }
        return ans;
    }
};