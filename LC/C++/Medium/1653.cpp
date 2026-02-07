class Solution {
public:
    int minimumDeletions(string s) {
        int n = s.size();
        int ans = n;

        int a = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == 'a') ++a;
        }

        int b = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'a') --a;
            ans = min(ans, a + b);
            if (s[i] == 'b') ++b;
        }


        return ans;
    }
};