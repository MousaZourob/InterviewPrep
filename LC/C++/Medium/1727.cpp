class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int ans = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] != 0 && i > 0) {
                    matrix[i][j] += matrix[i-1][j];
                }
            }

            vector<int> currRow = matrix[i];
            std::sort(currRow.begin(), currRow.end(), greater());
            for (int i = 0; i < n; i++) {
                ans = max(ans, currRow[i] * (i + 1));
            }
        }

        return ans;
    }
};