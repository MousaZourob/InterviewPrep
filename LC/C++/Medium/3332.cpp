class Solution {
public:
    int maxScore(int n, int k, vector<vector<int>>& stayScore, vector<vector<int>>& travelScore) {
        std::vector<std::vector<int>> dp(n, std::vector<int>(k + 1, 0));
        
        for (int currDay = k - 1; currDay >= 0; --currDay) {
            for (int currCity = 0; currCity < n; ++currCity) {
                int opt1 = stayScore[currDay][currCity] + dp[currCity][currDay + 1];
                int opt2 = 0;
                for (int dest = 0; dest < n; ++dest) {
                    if (dest != currCity) {
                        opt2 = max(opt2, travelScore[currCity][dest] + dp[dest][currDay + 1]);
                    }
                }
                dp[currCity][currDay] = std::max(opt1, opt2);
            }
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = std::max(ans, dp[i][0]);
        }
        return ans;
    }
};