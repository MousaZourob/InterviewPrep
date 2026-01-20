#include <algorithm>
#include <cmath>
#include <iostream>

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *std::max_element(piles.begin(), piles.end());
        int ans = right;

        while (left <= right) {
            int guess = (left + right) / 2;
            double hours_taken = 0;
            for (auto& bananas : piles) {
                hours_taken += std::ceil((double)bananas / guess);
            }

            if (hours_taken <= h) {
                ans = min(ans, guess);
                right = guess - 1;
            } else {
                left = guess + 1;
            }
        }
        return ans;
    }
};
