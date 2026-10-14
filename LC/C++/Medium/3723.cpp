class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9 * num) {
            return "";
        }
        std::string ans(sum / 9, '9');
        int r = sum % 9;
        if (r > 0) {
            ans += '0' + r;
        }
        ans.append(num - (int)ans.size(), '0');
        return ans;
    }
};