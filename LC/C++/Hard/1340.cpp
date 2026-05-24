class Solution {
    int n_;
    std::vector<int> cache_;
public:
    int dfs(vector<int>& arr, int d, int i) {
        if (cache_[i] != 0) {
            return cache_[i];
        }

        int res = 1;

        for (int step = 1; step <= d; ++step) {
            int j = i + step;
            if (j >= n_ || arr[j] >= arr[i]) {
                break;
            }

            res = max(res, 1 + dfs(arr, d, j));
        }

        for (int step = 1; step <= d; ++step) {
            int j = i - step;
            if (j < 0 || arr[j] >= arr[i]) {
                break;
            }

            res = max(res, 1 + dfs(arr, d, j));
        }

        cache_[i] = res;
        return res;
    }
 
    int maxJumps(vector<int>& arr, int d) {
        n_ = arr.size();
        cache_.assign(n_, 0);
        
        int ans = 1;
        for (int i = 0; i < n_; ++i) {
            ans = std::max(ans, dfs(arr, d, i));
        }

        return ans;
    }
};