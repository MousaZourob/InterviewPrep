class Solution {
public:
    int numberOfSubstrings(string s) {
        int ans = 0;

        std::unordered_map<char, int> count;
        int l = 0;
        for (int r = 0; r < s.size(); r++) {
            count[s[r]]++;
            while (count['a'] > 0 && count['b'] > 0 && count['c'] > 0) {
                count[s[l]]--;
                l++;
            }
            ans += l;
        }

        return ans;
    }
};