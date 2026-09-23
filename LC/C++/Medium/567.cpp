class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        std::array<int, 26> target{};
        std::array<int, 26> window{};

        for (char c : s1)
            target[c - 'a']++;

        int l = 0;
        for (int r = 0; r < s2.size(); ++r) {
            window[s2[r] - 'a']++;

            if (r >= s1.size()) {
                window[s2[l] - 'a']--;
                l++;
            }

            if (window == target)
                return true;
        }

        return false;
    }
};