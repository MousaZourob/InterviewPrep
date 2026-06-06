class Solution {
    int m, n;
public:
    std::set<std::pair<int, int>> find(vector<vector<int>>& board) {
        std::set<std::pair<int, int>> res;

        for (int i = 1; i < m - 1; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 0) continue;
                if (board[i][j] == board[i-1][j] && board[i][j] == board[i + 1][j]) {
                    res.insert({i - 1, j});
                    res.insert({i, j});
                    res.insert({i + 1, j});
                }
            }
        }
        
        for (int i = 0; i < m; ++i) {
            for (int j = 1; j < n - 1; ++j) {
                if (board[i][j] == 0) continue;
                if (board[i][j] == board[i][j - 1] && board[i][j] == board[i][j + 1]) {
                    res.insert({i, j - 1});
                    res.insert({i, j});
                    res.insert({i, j + 1});
                }
            }
        }

        return res;
    }

    void crush(vector<vector<int>>& board, std::set<std::pair<int, int>>& crushed) {
        for (auto& [i, j] : crushed) {
            board[i][j] = 0;
        }
    }

    void drop(vector<vector<int>>& board) {
        for (int j{}; j < n; ++j) {
            int zero = -1;
            for (int i = m - 1; i >= 0; --i) {
                if (board[i][j] == 0) { 
                    zero = std::max(zero, i);
                } else if (zero >= 0) {
                    int oldVal = board[i][j];
                    board[i][j] = 0;
                    board[zero][j] = oldVal;
                    zero--;
                }
            }
        }
    }

    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        m = board.size();
        n = board[0].size();

        std::set<std::pair<int, int>> crushed = find(board);
        while (!crushed.empty()) {
            crush(board, crushed);
            drop(board);
            crushed = find(board);
        }

        return board;
    }
};