class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        sorted_indices = sorted(
            range(number_of_people), key=lambda i: heights[i], reverse=True
        )

        return [names[i] for i in sorted_indices]