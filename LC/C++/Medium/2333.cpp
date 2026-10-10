class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        std::vector<int> diffs(n);
        long long k = (long long)k1 + k2;
        int maxDiff = 0;

        for (size_t i = 0; i < n; ++i) {
            int d = std::abs(nums1[i] - nums2[i]);
            diffs[i] = d;
            maxDiff = std::max(maxDiff, d);
        }

        int l = 0, r = maxDiff;
        while (l < r) {
            int mid = l + (r - l) / 2;
            long long ops = 0;

            for (int d : diffs) {
                ops += max(0, d - mid);
            }

            if (ops <= k) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        long long ans = 0;
        for (int& d : diffs) {
            if (d > l) {
                k -= d - l;
                d = l;
            }
        }

        for (int& d : diffs) {
            if (d == l && k > 0 && l > 0) {
                --d;
                --k;
            }
            ans += 1LL * d * d;
        }

        return ans;
    }
};