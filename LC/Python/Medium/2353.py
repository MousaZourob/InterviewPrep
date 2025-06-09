from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisine_dishes = defaultdict(SortedSet)
        
        for i in range(len(foods)):
            self.food_info[foods[i]] = [ratings[i], cuisines[i]]
            self.cuisine_dishes[cuisines[i]].add((-ratings[i], foods[i]))
        print(self.food_info)
        print(self.cuisine_dishes)
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_name = self.food_info[food][1]
        self.cuisine_dishes[cuisine_name].remove((-self.food_info[food][0], food))
        
        self.food_info[food][0] = newRating
        self.cuisine_dishes[cuisine_name].add((-self.food_info[food][0], food))

    def highestRated(self, cuisine: str) -> str:        
        return self.cuisine_dishes[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)