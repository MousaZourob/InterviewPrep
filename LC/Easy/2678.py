class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_count = 0

        for passenger_info in details:
            age_tens = ord(passenger_info[11]) - ord("0")
            age_ones = ord(passenger_info[12]) - ord("0")

            age = age_tens * 10 + age_ones

            if age > 60:
                senior_count += 1

        return senior_count