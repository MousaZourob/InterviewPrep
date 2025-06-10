class Solution {
public:
    int maxDifference(string s) {
        std::unordered_map<char, int> count;
        for (char c : s) {
            count[c]++;
        }

        int a1 = 0;
        int a2 = INT_MAX;
        
        for (const auto& [ch, v]: count) {
            if (v % 2 == 1) {
                a1 = std::max(a1, v);
            } else {
                a2 = std::min(a2, v);
            }
        }

        return a1 - a2;
    }
};