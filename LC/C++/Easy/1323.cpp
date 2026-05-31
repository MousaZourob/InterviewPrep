class Solution {
public:
    int maximum69Number (int num) {
        int temp = num;
        int place = 1;
        int targetPlace = 0;

        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 6) {
                targetPlace = place;
            }
            temp /= 10;
            place *= 10;
        }

        return num + 3 * targetPlace;
    }
};