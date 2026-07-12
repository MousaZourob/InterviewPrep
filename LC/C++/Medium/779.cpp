class Solution {
public:
    int kthGrammar(int n, int k) {
        int ans = 0;
        while (n > 1) {
            int half = 1 << (n - 2);
            if (k > half) {
                ans ^= 1;
                k -= half;
            }
            n--;
        }

        return ans;
    }
};