class Solution {
public:
    long long countCommas(long long n) {
        if (n < 1e3) {
            return 0;
        } 
        
        using LL = long long;
        long long ans = 0;
        if (n == 1e15) {
            ans += 5;
        }
        if (n >= 1e12) {
            ans += (std::min(n, LL(1e15 - 1)) - 1e12) * 4 + 4; 
        } 
        if (n >= 1e9) {
            ans += (std::min(n, LL(1e12 - 1)) - 1e9) * 3 + 3;
        }
        if (n >= 1e6) {
            ans += (std::min(n, LL(1e9 - 1)) - 1e6) * 2 + 2;
        }
        if (n >= 1e3) {
            ans += (std::min(n, LL(1e6 - 1)) - 1e3) + 1;
        }

        return ans;
    }
};