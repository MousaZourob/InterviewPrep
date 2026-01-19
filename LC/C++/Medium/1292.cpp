class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();

        vector<vector<int>> squareSum(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                squareSum[i][j] = mat[i-1][j-1] 
                                + squareSum[i-1][j] 
                                + squareSum[i][j-1] 
                                - squareSum[i-1][j-1];        
            }
        }

        int ans = 0;
        int limit = min(m, n);

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = ans + 1; k <= limit; ++k) {
                    if (i + k > m || j + k > n) break;

                    int currSum =
                        squareSum[i + k][j + k]
                      - squareSum[i][j + k]
                      - squareSum[i + k][j]
                      + squareSum[i][j];

                    if (currSum <= threshold) {
                        ans = k;
                    } else {
                        break;
                    }
                }
            }
        }

        return ans;
    
    }
};