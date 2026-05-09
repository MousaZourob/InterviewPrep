/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
    std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    std::set<std::pair<int, int>> visited{};
public:
    void dfs(Robot& robot, int x, int y, int dirr) {
        robot.clean();
        visited.insert({x, y});
        for (int i = 0; i < 4; ++i) {
            int newDir = (dirr + i) % 4;
            int nx = x + dirs[newDir].first;
            int ny = y + dirs[newDir].second;
            if (visited.find({nx, ny}) == visited.end()) {
                if (robot.move()) {
                    dfs(robot, nx, ny, newDir);
                    robot.turnRight();
                    robot.turnRight();
                    robot.move();
                    robot.turnRight();
                    robot.turnRight();
                }
            }
            robot.turnRight();
        }
    }

    void cleanRoom(Robot& robot) {
        int x = 0;
        int y = 0;
        int dirr = 0;
        dfs(robot, x, y, dirr);
    }
};