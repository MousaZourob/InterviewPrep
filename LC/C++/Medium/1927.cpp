class Solution {
public:
    bool sumGame(string num) {
        int n = num.size(); 
        int diff = 0;
        int q = 0;
        for (int i = 0; i < n; ++i) {
            int sign = (i < n / 2) ? 1 : -1;
            if (num[i] == '?') q += sign;
            else diff += sign * (num[i] - '0');
        }

        return diff * 2 != -9 * q;
    }
};