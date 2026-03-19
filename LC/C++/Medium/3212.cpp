class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> xCol(n, 0), yCol(n, 0);
        int ans = 0;

        for (int i = 0; i < m; ++i) {
            int xRow = 0, yRow = 0;

            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 'X') xCol[j]++;
                else if (grid[i][j] == 'Y') yCol[j]++;

                xRow += xCol[j];
                yRow += yCol[j];

                if (xRow > 0 && xRow == yRow) {
                    ans++;
                }
            }
        }

        return ans;
    }
};