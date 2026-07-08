class Solution {
public:
    long long sumAndMultiply(int n) {
        long long sum = 0;
        long long ans = 0;
        int count = 1;
        
        while (n > 0) {
            int curr = n % 10;
            if (curr != 0) {
                sum += curr;
                ans += count * curr;
                count *= 10;
            }
            n /= 10;
        }

        return ans * sum;
    }
};