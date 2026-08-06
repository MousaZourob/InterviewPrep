class Solution {
public:
    int smallestNumber(int n, int t) {
        for (int curr = n; ; curr++) {
            int num = curr;
            int product = 1;

            while (num > 0) {
                product *= num % 10;
                num /= 10;
            }

            if (product % t == 0) {
                return curr;
            }
        }

        return -1;
    }
};