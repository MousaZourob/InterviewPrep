class Solution {
public:
    int findKthNumber(int n, int k) {
        int curr = 1;
        k -= 1;

        while (k > 0) {
            int64_t steps = count_steps(n, curr, curr + 1);
            if (steps <= k) {
                curr += 1;
                k -= steps;
            } else {
                curr *= 10;
                k -= 1;
            }
        }

        return curr;
    }

    int64_t count_steps(int64_t n, int64_t left, int64_t right) {
        int64_t steps = 0;
        while (left <= n) {
            steps += min(n + 1, right) - left;
            left *= 10;
            right *= 10;
        }
        
        return steps;
    }
};