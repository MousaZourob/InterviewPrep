class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> ans;

        int i = 0, j = -1;
        int dirr = 1;

        while (0 < m*n) {
            for (int k = 0; k < n; ++k) {
                j += dirr;
                ans.emplace_back(matrix[i][j]);
            }
            --m;

            for (int k = 0; k < m; ++k){
                i += dirr;
                ans.emplace_back(matrix[i][j]);
            }
            --n;

            dirr *= -1;
        }

        return ans;
    }
};