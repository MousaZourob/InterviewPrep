class Solution {
public:
    int minOperations(string s) {
        if (std::ranges::is_sorted(s)) {
            return 0;
        }

        size_t n = s.size();
        char max = 'a', min = 'z';
        for (char c : s) {
            if (c < min) min = c;
            if (c > max) max = c;
        }

        if (n == 2) return -1;
        
        if (s[0] == min || s[n - 1] == max) return 1;

        for (size_t i = 1; i < n - 1; ++i) {
            if (s[i] == min || s[i] == max) {
                return 2;
            }
        }
        
        return 3;
    }
};