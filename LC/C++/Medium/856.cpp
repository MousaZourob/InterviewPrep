class Solution {
public:
    int scoreOfParentheses(string s) {
        int ans = 0;
        int curr = 0;
        
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                curr++;
            } else {
                curr--;
                if (s[i-1] == '(') {
                    ans += 1 << curr;
                }
            }
        }

        return ans;
    }
};