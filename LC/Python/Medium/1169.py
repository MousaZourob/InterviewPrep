class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        records = {}

        for t in transactions:
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)
            
            if time not in records:
                records[time] = {}
            if name not in records[time]:
                records[time][name] = []
            records[time][name].append(city)

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                ans.append(transaction)
                continue
            
            for t in range(time - 60, time + 61):
                if t in records and name in records[t]:
                    if len(records[t][name]) > 1 or (records[t][name][0] != city):
                        ans.append(transaction)
                        break

        return ans
