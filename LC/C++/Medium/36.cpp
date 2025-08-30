class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rows(9, vector<int>(9, 0));
        vector<vector<int>> cols(9, vector<int>(9, 0));
        vector<vector<int>> boxes(9, vector<int>(9, 0));

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int num = board[r][c] - '1';

                if (rows[r][num] == 1) return false;
                rows[r][num] = 1;

                if (cols[c][num] == 1) return false;
                cols[c][num] = 1;

                int box = (r / 3) * 3 + (c / 3);
                if (boxes[box][num] == 1) return false;
                boxes[box][num] = 1;
            }
        }

        return true;
    }
};