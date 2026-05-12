class Spreadsheet {
    std::vector<std::vector<int>> sheet_;
public:
    Spreadsheet(int rows) : sheet_(rows, std::vector<int>(26, 0)) {}
    
    void setCell(string cell, int value) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;
        sheet_[row][col] = value;
    }
    
    void resetCell(string cell) {
        int col = cell[0] - 'A';
        int row = stoi(cell.substr(1)) - 1;

        sheet_[row][col] = 0;
    }
    
    int eval(std::string s) {
        if (isdigit(s[0])) {
            return stoi(s);
        }

        int col = s[0] - 'A';
        int row = stoi(s.substr(1)) - 1;

        return sheet_[row][col];
    }

    int getValue(string formula) {
        int plus = formula.find('+');

        std::string x = formula.substr(1, plus - 1);
        std::string y = formula.substr(plus + 1);

        return eval(x) + eval(y);
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */