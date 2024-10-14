class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        def find_index(h):
            l, r = 0, len(monsters) - 1
            
            while l <= r:
                m = l + (r - l) // 2
                
                if monsters[m] > h:
                    r = m - 1
                else:
                    l  = m + 1
            return l
        
        ans = []
        monsters, coins = zip(*sorted(zip(monsters, coins)))
        coins = list(accumulate(coins, initial = 0))
        
        for hero in heroes:
            i = find_index(hero)
            ans.append(coins[i])

        return ans