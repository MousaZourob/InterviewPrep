class Solution {
public:
    int reverseDegree(string s) {
        int ans = 0;
        for (size_t i{}; i < s.size(); ++i) {
            ans += ('z' - s[i] + 1) * (i + 1);
        }

        return ans;
    }
};