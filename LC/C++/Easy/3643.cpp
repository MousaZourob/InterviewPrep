class Solution {
public:
    vector<vector<int>> reverseSubmatrix(vector<vector<int>>& grid, int x, int y, int k) {
        for (int col = y; col < k+y; ++col) {
            for (int row = x, row2 = x + k - 1; row < row2; ++row, --row2) {
                swap(grid[row][col], grid[row2][col]);
            }
        }

        return grid;
    }
};