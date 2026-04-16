class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int i = 0, j = 0;

        while (i < n) {
            int count = 1;
            while (i < n - 1 && chars[i] == chars[i + 1]) {
                count++;
                i++;
            }

            chars[j] = chars[i];
            j++;

            if (count > 1) {
                for (char c : to_string(count)) {
                    chars[j] = c;
                    j++;
                }
            }
            i++;
        }

        return j;
    }
};