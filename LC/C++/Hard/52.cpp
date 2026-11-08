class Solution {
    std::vector<bool> cols{};
    std::vector<bool> posDiag{};
    std::vector<bool> negDiag{};
    int ans;

    void dfs(int row, int n) {
        if (row == n) {
            ans++;
            return;
        }

        for (int i = 0; i < n; ++i) {
            int posD = row + i;
            int negD = row - i + n - 1;

            if (!cols[i] && !posDiag[posD] && !negDiag[negD]) {
                cols[i] = true;
                posDiag[posD] = true;
                negDiag[negD] = true;

                dfs(row + 1, n);
                
                cols[i] = false;
                posDiag[posD] = false;
                negDiag[negD] = false;
            }
        }

    }
public:
    int totalNQueens(int n) {
        cols.resize(n);
        posDiag.resize(2 * n - 1);
        negDiag.resize(2 * n - 1);

        dfs(0, n);

        return ans;
    }
};