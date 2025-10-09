class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = [(spell, index) for index, spell in enumerate(spells)]
        sorted_spells.sort()
        potions.sort()

        ans = [0] * len(spells)
        m = len(potions)
        potion_i = m - 1
        
        for spell, i in sorted_spells:
            while potion_i >= 0 and (spell * potions[potion_i]) >= success:
                potion_i -= 1
            ans[i] = m - (potion_i + 1)

        return ans