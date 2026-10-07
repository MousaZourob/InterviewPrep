class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0;
        int openNeeded = 0;

        for (auto& c : s) {
            if (c == '(') {
                open++;
            } else {
                if (open > 0) {
                    open--;
                } else {
                    openNeeded++;
                }
            }
        }

        return open + openNeeded;
    }
};