class Solution {
    int myGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }
public:

    int findGCD(vector<int>& nums) {
        int minNum = nums[0];
        int maxNum = nums[0];

        for (int num : nums) {
            minNum = std::min(minNum, num);
            maxNum = std::max(maxNum, num);
        }

        return myGCD(maxNum, minNum);
    }
};