class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int volume, int k) {
        for (int a = 0; a < volume; ++a) {
            int minLeft = heights[k];
            int minRight = heights[k];
            int idx = k;
            for (int i = k-1 ; i >= 0; --i) {
                if (heights[i] < minLeft) {
                    minLeft = heights[i];
                    idx = i;
                } else if (heights[i] > minLeft) {
                    break;
                }
            }

            if (idx != k) {
                heights[idx] += 1;
                continue;
            }

            for (int i = k+1 ; i < heights.size(); ++i) {
                if (heights[i] < minRight) {
                    minRight = heights[i];
                    idx = i;
                } else if (heights[i] > minRight) {
                    break;
                }
            }

            heights[idx] += 1;
        }

        return heights;
    }
};