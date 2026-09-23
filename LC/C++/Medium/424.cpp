class Solution {
public:
    int characterReplacement(string s, int k) {
        int ans = 0;
        std::unordered_map<char, int> seen{};
        int l = 0;
        int maxSeen = 0;

        for (int r{}; r < s.size(); ++r) {
            maxSeen = std::max(maxSeen, ++seen[s[r]]);
            while (r - l + 1 - maxSeen > k) {
                seen[s[l]]--;
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }

        return ans;
    }
};