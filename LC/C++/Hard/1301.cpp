class Solution {
    std::vector<std::pair<int,int>> dirs{{-1,0},{0,-1},{-1,-1}};
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int n = board.size(), MOD = 1e9 + 7;

        vector<vector<pair<int,int>>> dp(n, vector<pair<int,int>>(n, {0, 0}));
        dp[n-1][n-1] = {0, 1};

        for (int r = n-1; r >= 0; r--) {
            for (int c = n-1; c >= 0; c--) {
                if (board[r][c] == 'X' || dp[r][c].second == 0) continue;

                int sum = dp[r][c].first;
                int count = dp[r][c].second;
                
                for (auto& [dr, dc] : dirs) {
                    int nr = r+dr, nc = c+dc;
            
                    if (nr < 0 || nc < 0 || board[nr][nc] == 'X') continue;
            
                    int add = (board[nr][nc] >= '1' && board[nr][nc] <= '9') ? board[nr][nc] - '0' : 0;
                    int newsum = sum + add;
                    if (newsum > dp[nr][nc].first) {
                        dp[nr][nc] = {newsum, count};
                    } else if (newsum == dp[nr][nc].first) {
                        dp[nr][nc].second = (dp[nr][nc].second + count) % MOD;
                    }
                }
            }
        }

        return {dp[0][0].first % MOD, dp[0][0].second};
    }
};