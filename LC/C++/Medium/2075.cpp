class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        if (rows == 1) return encodedText;

        int n = encodedText.size();
        int cols = n / rows;

        std::string ans;
        ans.reserve(n);

        for (int c = 0; c < cols; ++c) {
            int r = 0, j = c;
            while (r < rows && j < cols) {
                ans += encodedText[r * cols + j];
                ++r;
                ++j;
            }
        }

        while (!ans.empty() && ans.back() == ' ') {
            ans.pop_back();
        }
        return ans;
    }
};