class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        std::vector<int> ans(n, 0);
        std::vector<bool> perm(n, 0);
        int count = 0;

        for (int i = 0; i < n; ++i) {
            if (perm[A[i] - 1]) {
                count++;
            }
            perm[A[i]-1] = true;
            if (perm[B[i] - 1]) {
                count++;
            }
            perm[B[i]-1] = true;

            ans[i] = count;
        }


        return ans;
    }
};