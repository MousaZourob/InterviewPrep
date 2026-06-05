class Solution {
public:
    int totalWaviness(int num1, int num2) {
        auto peaks = [](int x) -> int {
            std::string num = to_string(x);
            int count = 0;
            for (int i = 1; i < num.size() - 1; ++i) {
                bool peak = (num[i] > num[i-1] && num[i] > num[i+1]);  
                bool valley = (num[i] < num[i-1] && num[i] < num[i+1]);  

                if (peak || valley) count++;
            }

            return count;
        };
        int ans = 0;
        for (int i = num1; i <= num2; ++i) {
            ans += peaks(i);
        }
        return ans;
    }
};