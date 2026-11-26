class Solution {
public:
    bool canAliceWin(int n) {
        bool turn = false;
        int take = 10;

        while (n >= take) {
            n -= take;
            take--;
            turn = !turn;
        }

        return turn;
    }
};