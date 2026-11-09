class Solution {
    std::vector<std::vector<bool>> rows;
    std::vector<std::vector<bool>> cols;
    std::vector<std::vector<bool>> boxes;

    bool backtrack(std::vector<std::vector<char>>& board, int i, int j) {
        if (i == 9) {
            return true;
        }

        int new_i = i + (j + 1) / 9;
        int new_j = (j + 1) % 9;

        if (board[i][j] != '.') {
            return backtrack(board, new_i, new_j);
        }

        int box = (i / 3) * 3 + (j / 3);

        for (int guess = 1; guess <= 9; ++guess) {
            if (rows[i][guess] || cols[j][guess] || boxes[box][guess]) {
                continue;
            }


            rows[i][guess] = true;
            cols[j][guess] = true;
            boxes[box][guess] = true;
            board[i][j] = '0' + guess;

            if (backtrack(board, new_i, new_j)) {
                return true;
            }

            rows[i][guess] = false;
            cols[j][guess] = false;
            boxes[box][guess] = false;
            board[i][j] = '.';
        }

        return false;
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        rows.assign(9, std::vector<bool>(10, false));
        cols.assign(9, std::vector<bool>(10, false));
        boxes.assign(9, std::vector<bool>(10, false));

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') continue;

                int val = board[r][c] - '0';
                int box = (r / 3) * 3 + (c / 3);

                rows[r][val] = true;
                cols[c][val] = true;
                boxes[box][val] = true;
            }
        }

        backtrack(board, 0, 0);
    }
};