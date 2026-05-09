class Solution {
public:
    vector<long long> minimumCosts(vector<int>& r, vector<int>& e, int ec) {
        int n = r.size();

        vector<vector<long long>> dp(n + 1, vector<long long>(2, -1));
        vector<long long> ans(n);

        long long prevRegular = 0;
        long long prevExpress = ec;

        for (int i = 0; i < n; i++) {
            long long rRoute =
                min(prevRegular, prevExpress) + r[i];

            long long eRoute =
                min(prevExpress, prevRegular + ec) + e[i];

            ans[i] = min(rRoute, eRoute);

            prevRegular = rRoute;
            prevExpress = eRoute;
        }

        return ans;
    }
};