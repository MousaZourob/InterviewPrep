class Solution {
public:
    double angleClock(int hour, int minutes) {
        double minJump = 6;
        double hourJump = 30;

        double minAngle = minJump * minutes;
        double hourAngle = (hour % 12 + minutes/60.0) * hourJump;

        double ans = std::abs(minAngle - hourAngle);
        return std::min(ans, 360-ans);
    }
};