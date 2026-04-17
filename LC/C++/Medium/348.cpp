class TicTacToe {
    int n_;
    int* rows_;
    int* cols_;
    int diagonal = 0;
    int antiDiagonal = 0;
public:
    TicTacToe(int n) : n_(n), rows_(new int[n]()), cols_(new int[n]()) {}
    
    int move(int row, int col, int player) {
        int p = player == 1 ? 1 : -1;

        rows_[row] += p;
        cols_[col] += p;

        if (row == col) diagonal += p;
        if (row + col == n_ - 1) antiDiagonal += p;

        if (abs(rows_[row]) == n_ || abs(cols_[col]) == n_ || abs(diagonal) == n_ || abs(antiDiagonal) == n_) return player;

        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */