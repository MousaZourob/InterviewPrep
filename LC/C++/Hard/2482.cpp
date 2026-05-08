class Solution {
public:
    int countPalindromes(string s) {
        const int MOD = 1e9 + 7;
        int n = s.size();

        vector<vector<long long>> right(n, vector<long long>(100, 0));
        vector<int> countR(10, 0);

        for (int i = n - 1; i >= 0; --i) {
            if (i + 1 < n) right[i] = right[i + 1];

            int d = s[i] - '0';
            for (int x = 0; x < 10; ++x) {
                right[i][d * 10 + x] += countR[x];
            }
            countR[d]++;
        }

        long long ans = 0;
        vector<long long> left(100, 0);
        vector<int> countL(10, 0);

        for (int mid = 0; mid < n; ++mid) {
            int d = s[mid] - '0';

            for (int a = 0; a < 10; ++a) {
                for (int b = 0; b < 10; ++b) {
                    int leftPair = a * 10 + b;
                    int rightPair = b * 10 + a;
                    if (mid + 1 < n) {
                        ans = (ans + left[leftPair] * right[mid + 1][rightPair]) % MOD;
                    }
                }
            }

            for (int x = 0; x < 10; ++x) {
                left[x * 10 + d] += countL[x];
            }
            countL[d]++;
        }

        return ans;
    }
};