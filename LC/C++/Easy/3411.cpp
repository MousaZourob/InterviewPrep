class Solution {
public:
    int maxLength(vector<int>& nums) {
        int ans = 0;

        for (int i = 0; i < nums.size(); ++i) {
            long long prod = 1;
            long long g = 0;
            long long l = 1;

            for (int j = i; j < nums.size(); ++j) {
                auto num = nums[j];

                prod *= num;
                g = gcd(g, (long long)num);
                l = lcm(l, (long long)num);

                if (prod == g * l)
                    ans = max(ans, j - i + 1);

                if (prod > g * l)
                    break;
            }
        }

        return ans;
    }
};