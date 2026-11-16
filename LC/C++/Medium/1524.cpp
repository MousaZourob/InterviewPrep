class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {   
        constexpr int MOD = 1e9 + 7;
        int count[2] = {1, 0};
        int parity = 0, ans = 0;

        for (int num : arr) {
            parity = (parity + num) % 2;
            ans = (ans + count[1 - parity]) % MOD;

            count[parity]++;
        }

        return ans;
    }
};