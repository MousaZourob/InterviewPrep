class Solution {
public:
    int minimumPushes(string word) {
        std::vector<int> frequency(26);

        for (char c : word) {
            frequency[c - 'a']++;
        }

        std::sort(frequency.begin(), frequency.end(), std::greater<int>{});

        int ans = 0;

        for (int i = 0; i < 26 && frequency[i] > 0; i++) {
            ans += frequency[i] * (i / 8 + 1);
        }

        return ans;
    }
};