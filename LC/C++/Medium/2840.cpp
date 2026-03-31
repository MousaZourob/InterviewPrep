class Solution {
public:
    bool checkStrings(string s1, string s2) {
        int n = s1.size();

        if (n != s2.size()) {
            return false;
        }

        std::array<int, 52> counts{};

        for (int i = 0; i < n; ++i) {
            int offset = (i % 2) * 26;
            counts[s1[i] - 'a' + offset]++;
            counts[s2[i] - 'a' + offset]--;
        }

        for (auto& c : counts) {
            if (c != 0) {
                return false;
            }
        }

        return true;
    }
};