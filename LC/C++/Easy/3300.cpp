class Solution {
public:
    int minElement(vector<int>& nums) {
        int ans = INT_MAX;

        for (int x : nums) {
            int res = 0;
            while (x > 0) {
                res += x % 10;
                x /= 10;
            }
            ans = min(ans, res);
        }

        return ans;
    }
};