class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        count = Counter(hand)
        hand.sort()
        
        i = 0
        while i < len(hand):
            min_num = hand[i]
            
            for j in range(groupSize):
                if min_num+j not in count:
                    return False
                
                count[min_num+j] -= 1

                if count[min_num+j] == 0:
                    del count[min_num+j]

            while i < len(hand) and hand[i] not in count:
                i += 1
            
        
        return True