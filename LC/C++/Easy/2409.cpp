class Solution {
    std::vector<int> months{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int parse(std::string date) {
        int month = stoi(date.substr(0, 2)) - 1;
        int day = stoi(date.substr(3, 2));

        for (int i = 0; i < month; ++i) {
            day += months[i];
        }

        return day;
    }

public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int start = std::max(parse(arriveAlice), parse(arriveBob));
        int end = std::min(parse(leaveAlice), parse(leaveBob));

        return std::max(0, end - start + 1);
    }
};