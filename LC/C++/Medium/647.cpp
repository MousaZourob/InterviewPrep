class Solution {
    int n_;
    std::string s_;
public:
    int expand(int l, int r) {
        int count = 0;

        while (l >= 0 && r < n_ && s_[l] == s_[r]) {
            l--;
            r++;
            count++;
        }

        return count;
    }

    int countSubstrings(string s) {
        n_ = s.size();
        s_ = s;

        int ans = 0;

        for (int i = 0; i < n_; ++i) {
            ans += expand(i, i) + expand(i, i + 1);
        }

        return ans;
    }
};