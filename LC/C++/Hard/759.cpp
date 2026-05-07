/*
// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {
        std::vector<Interval> intervals{};
        intervals.reserve(schedule.size());
        for (auto& row : schedule) {
            for (auto& interval : row) {
                intervals.emplace_back(interval);
            }
        }

        std::sort(intervals.begin(), intervals.end(), 
            [](const Interval& a, const Interval& b) {
                return a.start < b.start;
            });

        std::vector<Interval> merged{};
        merged.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            if (merged.back().end >= intervals[i].start) {
                merged.back().end = max(merged.back().end, intervals[i].end);
            } else {
                merged.push_back(intervals[i]);
            }
        }

        std::vector<Interval> ans{};
        for (int i = 1; i < merged.size(); ++i) {
            ans.emplace_back(merged[i-1].end, merged[i].start);
        }

        return ans;
    }
};