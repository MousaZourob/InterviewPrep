class Solution {
public:
    string boldWords(vector<string>& words, string s) {
        int n = s.size();
        std::vector<bool> mask(n, false);

        for (auto& word : words) {
            size_t pos = s.find(word);

            while (pos != string::npos) {
                for (size_t i = pos; i < pos + word.size(); ++i) {
                    mask[i] = true;
                }

                pos = s.find(word, pos + 1);
            }
        }

        std::string ans{};

        for (int i = 0; i < n; ++i) {
            if (mask[i] && (i == 0 || !mask[i - 1])) {
                ans += "<b>";
            }

            ans += s[i];

            if (mask[i] && (i == n - 1 || !mask[i + 1])) {
                ans += "</b>";
            }
        }

        return ans;
    }
};