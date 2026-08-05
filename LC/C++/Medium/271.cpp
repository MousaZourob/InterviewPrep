class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        std::string ans{};

        for (auto& str : strs) {
            ans += to_string(str.size());
            ans += "$";
            ans += str;
        }

        return ans;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        std::vector<string> ans{};
        int i = 0;

        while (i < s.size()) {
            string len;

            while (isdigit(s[i])) {
                len += s[i++];
            }

            i++;

            int length = stoi(len);
            ans.push_back(s.substr(i, length));
            i += length;
        }

        return ans;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));