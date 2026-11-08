class Solution {
    std::vector<bool> cols{};
    std::vector<bool> posDiag{};
    std::vector<bool> negDiag{};
    std::vector<std::vector<std::string>> ans{};

    void dfs(std::vector<std::string>& board, int row, int n) {
        if (row == n) {
            ans.emplace_back(board);
            return;
        }

        for (int i = 0; i < n; ++i) {
            int posD = row + i;
            int negD = row - i + n - 1;

            if (!cols[i] && !posDiag[posD] && !negDiag[negD]) {
                cols[i] = true;
                posDiag[posD] = true;
                negDiag[negD] = true;
                board[row][i] = 'Q';

                dfs(board, row + 1, n);
                
                cols[i] = false;
                posDiag[posD] = false;
                negDiag[negD] = false;
                board[row][i] = '.';
            }
        }

    }
public:
    vector<vector<string>> solveNQueens(int n) {
        cols.resize(n);
        posDiag.resize(2 * n - 1);
        negDiag.resize(2 * n - 1);
        std::vector<std::string> board(n, std::string(n, '.'));

        dfs(board, 0, n);

        return ans;
    }
};