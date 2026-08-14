class Solution {
public:
    int maximumLengthSubstring(string s) {
        std::unordered_map<char, int> seen;
        int ans = 2;
        int l = 0;

        for (int r = 0; r < s.size(); ++r) {
            seen[s[r]]++;

            while (seen[s[r]] > 2) {
                seen[s[l]]--;
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }
        return ans;
    }
};