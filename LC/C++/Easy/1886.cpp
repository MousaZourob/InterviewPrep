class Solution {
    void rotate(vector<vector<int>>& matrix) {
        int left = 0, right = matrix.size() - 1;

        while (left < right) {
            int top = left;
            int bottom = right;

            for (int offset = 0; offset < right - left; ++offset) {
                int temp = matrix[top][left + offset];
        
                matrix[top][left + offset] = matrix[bottom - offset][left];
                matrix[bottom - offset][left] = matrix[bottom][right - offset];
                matrix[bottom][right - offset] = matrix[top + offset][right];
                matrix[top + offset][right] = temp;

            }

            left += 1;
            right -= 1;
        }
    }
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        if (mat == target) return true;

        for (int i = 0; i < 3; ++i) {
            rotate(mat);
            if (mat == target) return true;
        }

        return false;
    }
};