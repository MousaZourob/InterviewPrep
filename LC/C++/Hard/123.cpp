class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int fb = INT_MIN;
        int fs = 0;
        int sb = INT_MIN;
        int ss = 0;

        for (int price : prices) {
            fb = max(fb, -price);
            fs = max(fs, fb + price);
            sb = max(sb, fs - price);
            ss = max(ss, sb + price);
        }

        return ss;
    }
};