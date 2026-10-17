class Solution {
    int digitSum(int num) {
        int res = 0;

        while (num > 0) {
            res += num % 10;
            num /= 10;
        } 

        return res;
    }
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> target = nums;

        std::ranges::sort(target, [&](int a, int b) {
            int sumA = digitSum(a);
            int sumB = digitSum(b);

            if (sumA != sumB) {
                return sumA < sumB;
            }

            return a < b;
        });

        std::unordered_map<int, int> link{};
        for (int i = 0; i < n; ++i) {
            link[target[i]] = i;
        }

        std::vector<bool> visited(n, false);
        int ans = 0;

        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;

            int curr = i;
            int k = 0;

            while (!visited[curr]) {
                visited[curr] = true;
                curr = link[nums[curr]];
                k++;
            }

            ans += k - 1;
        }

        return ans;
    }
};