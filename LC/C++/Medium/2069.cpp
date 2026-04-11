class Robot {
    int w_, h_;
    int cycle_;
    int steps_ = 0;
    bool started_ = false;

public:
    Robot(int width, int height) : w_(width - 1), h_(height - 1) {
        cycle_ = 2 * (w_ + h_);
    }
    
    void step(int num) {
        started_ = true;
        steps_ = (steps_ + num) % cycle_;
    }
    
    vector<int> getPos() {
        int s = steps_;
        
        if (s <= w_) return {s, 0};
        s -= w_;
        
        if (s <= h_) return {w_, s};
        s -= h_;
        
        if (s <= w_) return {w_ - s, h_};
        s -= w_;
        
        return {0, h_ - s};
    }
    
    string getDir() {
        if (!started_) return "East";
        if (steps_ == 0) return "South";
        
        int s = steps_;
        if (s <= w_) return "East";
        s -= w_;
        if (s <= h_) return "North";
        s -= h_;
        if (s <= w_) return "West";
        return "South";
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */