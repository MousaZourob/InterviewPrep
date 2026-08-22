class Solution {
public:
    bool checkDivisibility(int n) {
        int curr = n;
        int sum = 0;
        int prod = 1;

        while (curr > 0) {
            int digit = curr % 10;
            prod *= digit;
            sum += digit;
            curr /= 10;
        }
        cout << sum << " " << prod << endl;
        return n % (sum + prod) == 0;
    }
};