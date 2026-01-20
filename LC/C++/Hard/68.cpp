class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        int i = 0;

        while (i < words.size()) {
            vector<string> currentLine = getWords(words, maxWidth, i);
            ans.emplace_back(createLine(words, maxWidth, currentLine, i));
        }

        return ans;
    }

private:
    vector<string> getWords(vector<string>& words, int maxWidth, int &i) {
        vector<string> currentLine{};
        int currLength = 0;

        while (i < words.size() && currLength + words[i].size() <= maxWidth) {
            currentLine.emplace_back(words[i]);
            currLength += words[i].size() + 1;
            i++;
        }

        return currentLine;
    }

     string createLine(vector<string>& words, int maxWidth, vector<string>& line, int i) {
        int base_length = -1;
        for (const string& w : line) {
            base_length += w.size() + 1;
        }

        int extra_spaces = maxWidth - base_length;

        if (line.size() == 1 || i == words.size()) {
            string res;
            for (int j = 0; j < line.size(); j++) {
                if (j) res += " ";
                res += line[j];
            }
            res += string(extra_spaces, ' ');
            return res;
        }

        int gaps = line.size() - 1;
        int spaces_per_gap = extra_spaces / gaps;
        int remainder = extra_spaces % gaps;

        for (int j = 0; j < remainder; j++) {
            line[j] += " ";
        }
        for (int j = 0; j < gaps; j++) {
            line[j] += string(spaces_per_gap, ' ');
        }

        string res;
        for (int j = 0; j < line.size(); j++) {
            if (j) res += " ";
            res += line[j];
        }
        return res;
    }

};