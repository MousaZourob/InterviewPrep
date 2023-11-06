class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        self.min_seat = 1
        

    def reserve(self) -> int:
        if self.seats:
            return heappop(self.seats)
        
        seat_num = self.min_seat
        self.min_seat += 1
        return seat_num
        
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)