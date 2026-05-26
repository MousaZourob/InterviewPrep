class Solution {
public:
    int numberOfSpecialChars(string word) {
        int ans = 0;
        std::vector<bool> lower(26, false);
        std::vector<bool> upper(26, false);

        for (char c : word) {
            if (islower(c)) lower[c - 'a'] = true;
            if (isupper(c)) upper[c - 'A'] = true;
        }

        for (int i = 0; i < 26; ++i) {
            if (lower[i] && upper[i]) ans++;
        }

        return ans;
    }
};