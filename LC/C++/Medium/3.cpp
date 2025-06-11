class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        int window_start = 0;
        unordered_set<char> seen = {};

        for (int i = 0; i < s.length(); i++) {
            while (seen.find(s[i]) != seen.end()) {
                seen.erase(s[window_start]);
                window_start++;
            }
            ans = max(ans, i - window_start + 1);
            seen.insert(s[i]);
        }

        return ans;
    }
};