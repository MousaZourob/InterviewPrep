class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int left = 0, right = 0;
        int place = 1;
        
        while (n > 0) {
            int temp = n % 10;
            n /= 10;

            if (temp <= 1 && n > 0) {
                temp += 10;
                n--;
            }

            int remain = temp % 2;
            left += (temp / 2) * place;
            right += (temp / 2 + remain) * place;

            place *= 10;
        }

        return {left, right};
    }
};